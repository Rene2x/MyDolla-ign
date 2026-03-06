#!/usr/bin/env python3
"""
My Dolla $ign - Interactive Budget Tutor Demo
Run: python demo.py

This script demonstrates the AI tutor by:
1. Letting users input their own budget data
2. Generating AI-powered analysis
3. Presenting 2-3 interactive quiz questions
4. Providing personalized tips
5. Allowing free-form Q&A with the AI
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from src.ai_tutor import AITutor

# Initialize AI model globally for reuse
import google.generativeai as genai
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("\n" + "=" * 60)
    print("        MY DOLLA $IGN - AI BUDGET TUTOR")
    print("=" * 60)
    print("  Your personal AI-powered financial education assistant")
    print("=" * 60 + "\n")


def get_float_input(prompt):
    """Get a float input from user."""
    try:
        value = input(f"{prompt}: $").strip()
        if value == "":
            print("  Please enter a value.")
            return get_float_input(prompt)
        return float(value.replace("$", "").replace(",", ""))
    except ValueError:
        print("  Invalid input, please enter a number.")
        return get_float_input(prompt)


def get_goal_input():
    """Get user's financial goal."""
    print("\nWhat's your main financial goal?")
    print("  1. Build emergency fund")
    print("  2. Pay off debt")
    print("  3. Save for retirement")
    print("  4. General savings")
    
    choice = input("\nEnter choice [1-4]: ").strip()
    goals = {
        "1": "emergency_fund",
        "2": "debt_payoff", 
        "3": "retirement",
        "4": "general_savings"
    }
    return goals.get(choice, "general_savings")


def collect_budget_data():
    """Collect budget data from user interactively."""
    print("\n" + "-" * 40)
    print(" STEP 1: Enter Your Monthly Budget")
    print("-" * 40)
    
    print("\nFirst, let's get your monthly income:")
    income = get_float_input("  Monthly income (after taxes)")
    
    print("\nNow, let's enter your monthly expenses:\n")
    
    expenses = {
        "rent": get_float_input("  Rent/Housing"),
        "food": get_float_input("  Food/Groceries"),
        "transportation": get_float_input("  Transportation"),
        "utilities": get_float_input("  Utilities"),
        "entertainment": get_float_input("  Entertainment"),
        "savings": get_float_input("  Current Savings"),
        "other": get_float_input("  Other expenses"),
    }
    
    goal = get_goal_input()
    
    total_expenses = sum(expenses.values())
    remaining = income - total_expenses
    
    return {
        "monthly_income": income,
        "total_expenses": total_expenses,
        "remaining": remaining,
        "goal": goal,
        "expenses": expenses
    }


def display_budget_summary(data):
    """Display a summary of the entered budget."""
    print("\n" + "-" * 40)
    print(" YOUR BUDGET SUMMARY")
    print("-" * 40)
    
    income = data["monthly_income"]
    print(f"\n  Monthly Income: ${income:,.2f}")
    print("\n  Expenses:")
    
    for category, amount in data["expenses"].items():
        pct = (amount / income * 100) if income > 0 else 0
        print(f"    - {category.title():15} ${amount:>8,.2f}  ({pct:5.1f}%)")
    
    print(f"\n  Total Expenses:  ${data['total_expenses']:,.2f}")
    print(f"  Remaining:       ${data['remaining']:,.2f}")
    print(f"  Goal:            {data['goal'].replace('_', ' ').title()}")


def generate_additional_questions(budget_data, existing_quiz, rules_used):
    """Generate 2 more quiz questions based on the budget data."""
    prompt = f"""You are a financial literacy tutor. Based on this user's budget data, generate 2 additional quiz questions.

USER BUDGET:
- Monthly Income: ${budget_data['monthly_income']}
- Expenses: {budget_data['expenses']}
- Goal: {budget_data['goal']}
- Total Expenses: ${budget_data['total_expenses']}
- Remaining: ${budget_data['remaining']}

Already asked: {existing_quiz.get('question', '')}

Generate 2 NEW questions (different from the one above) that test the user's understanding of:
1. One question about budgeting concepts (like 50/30/20 rule, needs vs wants)
2. One question specific to their numbers (calculations, percentages)

Return ONLY valid JSON in this exact format:
{{
  "questions": [
    {{
      "question": "Question 1 text here",
      "answer": "The correct answer",
      "rule_ids": ["R_50_30_20"]
    }},
    {{
      "question": "Question 2 text here", 
      "answer": "The correct answer",
      "rule_ids": ["R_HOUSING_COST"]
    }}
  ]
}}
"""
    
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                temperature=0.3,
            )
        )
        result = json.loads(response.text)
        return result.get("questions", [])
    except Exception as e:
        return []


def run_single_quiz(question_num, question, correct_answer, rules):
    """Run a single quiz question with AI answer checking."""
    print(f"\n{'='*60}")
    print(f" QUESTION {question_num}")
    print("=" * 60)
    
    print(f"\n{question}")
    print("\nType your answer (or press Enter to skip):")
    user_answer = input("\nYour answer: ").strip()
    
    if not user_answer:
        print("\nSkipped! Here's the answer:")
        print("-" * 40)
        print(f"\n{correct_answer}")
    else:
        print("\nChecking your answer...")
        
        check_prompt = f"""You are grading a student's answer to a financial literacy quiz.

Question: {question}
Correct Answer: {correct_answer}
Student's Answer: {user_answer}

Evaluate if the student's answer is correct, partially correct, or incorrect.
Be encouraging but honest. If they got the general idea right, give them credit.

Respond in this EXACT format:
VERDICT: [CORRECT / PARTIALLY CORRECT / INCORRECT]
FEEDBACK: [1-2 sentences of encouraging feedback]
"""
        
        try:
            response = model.generate_content(check_prompt)
            feedback = response.text.strip()
            
            print("\n" + "-" * 40)
            print(" AI FEEDBACK")
            print("-" * 40)
            print(f"\n{feedback}")
            
            print("\n" + "-" * 40)
            print(" CORRECT ANSWER")
            print("-" * 40)
            print(f"\n{correct_answer}")
            
        except Exception:
            print(f"\nCorrect answer: {correct_answer}")
    
    if rules:
        print(f"\nRules Referenced: {', '.join(rules)}")


def run_quiz_session(budget_data, initial_quiz, rules_used):
    """Run the full quiz session with 2-3 questions."""
    print("\n" + "=" * 60)
    print("           QUIZ TIME! (2-3 Questions)")
    print("=" * 60)
    print("\nLet's test your understanding of your budget!")
    input("\nPress Enter to start the quiz...")
    
    # Question 1: From the AI tutor
    run_single_quiz(
        1,
        initial_quiz.get("question", "No question"),
        initial_quiz.get("answer", "No answer"),
        initial_quiz.get("rule_ids", [])
    )
    
    # Generate additional questions
    print("\n\nGenerating more questions based on your budget...")
    additional_questions = generate_additional_questions(budget_data, initial_quiz, rules_used)
    
    # Questions 2 and 3
    for i, q in enumerate(additional_questions[:2], start=2):
        run_single_quiz(
            i,
            q.get("question", "No question"),
            q.get("answer", "No answer"),
            q.get("rule_ids", [])
        )
    
    # Quiz complete
    print("\n" + "=" * 60)
    print(" QUIZ COMPLETE!")
    print("=" * 60)
    print("\nGreat job working through those questions!")
    input("\nPress Enter to continue...")


def run_qa_session(budget_data):
    """Allow users to ask free-form questions to the AI."""
    print("\n" + "=" * 60)
    print("        ASK THE AI TUTOR")
    print("=" * 60)
    
    # First ask if they want to ask questions
    print("\nWould you like to ask any follow-up questions about")
    print("budgeting or your finances?")
    want_qa = input("\nAsk questions? (y/n): ").strip().lower()
    
    if want_qa not in ['y', 'yes']:
        print("\nNo problem! Moving on...")
        return
    
    print("\nGreat! Ask me anything about budgeting or your finances.\n")
    
    context = f"""You are My Dolla $ign, a friendly AI budget tutor. 
The user has this budget:
- Monthly Income: ${budget_data['monthly_income']}
- Total Expenses: ${budget_data['total_expenses']}
- Remaining: ${budget_data['remaining']}
- Goal: {budget_data['goal']}
- Expenses breakdown: {budget_data['expenses']}

Answer their questions about budgeting, their specific situation, or general financial literacy.
Keep answers concise (2-4 sentences) and educational.
Reference their actual numbers when relevant.
Do NOT give specific investment advice or recommend financial products.
"""
    
    while True:
        print("-" * 40)
        user_question = input("Your question: ").strip()
        
        if not user_question:
            continue
        
        print("\nAI is thinking...")
        
        try:
            response = model.generate_content(
                f"{context}\n\nUser question: {user_question}"
            )
            print("\n" + "-" * 40)
            print("AI TUTOR:")
            print("-" * 40)
            print(f"\n{response.text.strip()}\n")
        except Exception as e:
            print(f"\nSorry, I couldn't process that question. Try again!\n")
            continue
        
        # Ask if they want to continue
        print("-" * 40)
        continue_qa = input("Do you have another question? (y/n): ").strip().lower()
        
        if continue_qa not in ['y', 'yes']:
            print("\nThanks for your questions!")
            break


def main():
    clear_screen()
    print_header()
    
    # Check API key
    if not os.getenv("GEMINI_API_KEY"):
        print("ERROR: GEMINI_API_KEY not set in .env file")
        return
    
    print("Welcome! This demo will:")
    print("  1. Collect your budget information")
    print("  2. Analyze it using AI")
    print("  3. Quiz you with 2-3 questions")
    print("  4. Give you personalized tips")
    print("  5. Let you ask the AI any questions")
    
    input("\nPress Enter to begin...")
    
    # Collect data
    budget_data = collect_budget_data()
    display_budget_summary(budget_data)
    
    print("\n" + "=" * 60)
    print(" ANALYZING YOUR BUDGET WITH AI...")
    print("=" * 60)
    print("\n(This may take a few seconds...)\n")
    
    # Call AI Tutor
    try:
        tutor = AITutor()
        result = tutor.generate_session(budget_data)
    except Exception as e:
        print(f"\nError calling AI: {e}")
        return
    
    # Display AI Explanation
    print("\n" + "=" * 60)
    print(" AI ANALYSIS")
    print("=" * 60)
    print(f"\nStatus: {result.get('status', 'unknown')}")
    print(f"\n{result.get('explanation', 'No explanation available')}")
    
    input("\nPress Enter to continue to the quiz...")
    
    # Run Quiz Session (2-3 questions)
    quiz = result.get("quiz", {})
    rules_used = result.get("used_rule_ids", [])
    if quiz:
        run_quiz_session(budget_data, quiz, rules_used)
    
    # Display Tip
    print("\n" + "=" * 60)
    print(" PERSONALIZED TIP")
    print("=" * 60)
    
    tip = result.get("tip", {})
    print(f"\n{tip.get('text', 'No tip available')}")
    
    if tip.get("rule_ids"):
        print(f"\nBased on: {', '.join(tip['rule_ids'])}")
    
    # Summary of rules
    print("\n" + "=" * 60)
    print(" RULES USED IN THIS SESSION")
    print("=" * 60)
    if rules_used:
        for rule in rules_used:
            print(f"  - {rule}")
    else:
        print("  No specific rules cited")
    
    # Q&A Session
    run_qa_session(budget_data)
    
    # Closing
    print("\n" + "=" * 60)
    print(" Thank you for using My Dolla $ign!")
    print(" Remember: This is for educational purposes only.")
    print("=" * 60 + "\n")
    
    # Option to see full JSON
    see_json = input("Would you like to see the full AI response? (y/n): ").strip().lower()
    if see_json == 'y':
        print("\n" + "-" * 40)
        print("FULL JSON RESPONSE:")
        print("-" * 40)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
