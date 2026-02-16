"""
============================================
ASSIGNED TO: Member 3 (AI/ML Lead)

AI Service - Handles all AI/OpenAI API interactions.

This is the core AI integration for the project.

TODO (Member 3):
1. Design and refine the prompt for budget analysis
2. Test different prompt structures for better results
3. Handle edge cases (zero income, extreme values)
4. Optimize token usage to reduce costs
5. Add error handling for API failures
6. Consider caching common responses
============================================
"""

import os
from typing import Dict, List, Any
from openai import OpenAI

# Import the BudgetInput model
from app.models.budget import BudgetInput


def get_openai_client():
    """
    Get OpenAI client instance.
    
    TODO (Member 3): Add error handling if API key is missing
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    return OpenAI(api_key=api_key)


def build_budget_prompt(budget: BudgetInput) -> str:
    """
    Build the prompt for budget analysis.
    
    TODO (Member 3): This is the key prompt engineering task!
    Experiment with different prompt structures to get the best results.
    
    Args:
        budget: BudgetInput object with user's financial data
        
    Returns:
        Formatted prompt string for the AI
    """
    # Format expenses for the prompt
    expenses_text = "\n".join([
        f"- {category.replace('_', ' ').title()}: ${amount:.2f}"
        for category, amount in budget.expenses.items()
    ])
    
    # TODO (Member 3): Refine this prompt for better results
    prompt = f"""You are a friendly financial educator helping someone understand their budget.
Analyze the following budget data and provide educational insights.

IMPORTANT RULES:
1. Use simple, easy-to-understand language (no jargon)
2. Be encouraging and supportive
3. Provide specific, actionable tips
4. DO NOT give specific investment advice
5. Always remind the user this is for educational purposes only

USER'S BUDGET:
Monthly Income: ${budget.monthly_income:.2f}

Expenses:
{expenses_text}

Total Expenses: ${budget.total_expenses:.2f}
Remaining: ${budget.remaining:.2f}

Please provide:
1. A brief analysis of their spending patterns (2-3 paragraphs)
2. 3-4 key insights or tips based on their specific situation
3. An explanation of a relevant budgeting concept (like the 50/30/20 rule)

Keep your response concise and focused on education."""

    return prompt


def parse_ai_response(response_text: str, budget: BudgetInput) -> Dict[str, Any]:
    """
    Parse the AI response into structured data.
    
    TODO (Member 3): Improve parsing logic to extract insights as a list
    
    Args:
        response_text: Raw text from AI
        budget: Original budget input for calculating breakdowns
        
    Returns:
        Dictionary with analysis, breakdown, and insights
    """
    # Calculate expense breakdown
    breakdown = []
    for category, amount in sorted(
        budget.expenses.items(), 
        key=lambda x: x[1], 
        reverse=True
    ):
        if budget.monthly_income > 0:
            percentage = (amount / budget.monthly_income) * 100
        else:
            percentage = 0
            
        breakdown.append({
            'category': category.replace('_', ' ').title(),
            'amount': amount,
            'percentage': round(percentage, 1)
        })
    
    # TODO (Member 3): Parse insights from AI response as a list
    # For now, we'll use placeholder insights
    insights = [
        f"Your total expenses are ${budget.total_expenses:.2f} ({(budget.total_expenses/budget.monthly_income*100):.1f}% of income)" if budget.monthly_income > 0 else "Please enter your income to see percentage breakdowns",
        f"You have ${budget.remaining:.2f} remaining after expenses",
        "Consider the 50/30/20 rule: 50% for needs, 30% for wants, 20% for savings",
    ]
    
    return {
        'analysis': response_text,
        'breakdown': breakdown,
        'insights': insights
    }


def analyze_budget(budget: BudgetInput) -> Dict[str, Any]:
    """
    Main function to analyze a user's budget using AI.
    
    TODO (Member 3): 
    - Add retry logic for API failures
    - Add response time logging
    - Consider streaming for faster perceived response
    
    Args:
        budget: BudgetInput object with user's financial data
        
    Returns:
        Dictionary containing analysis, breakdown, and insights
    """
    try:
        # Get OpenAI client
        client = get_openai_client()
        
        # Build the prompt
        prompt = build_budget_prompt(budget)
        
        # Call OpenAI API
        # TODO (Member 3): Experiment with different models and parameters
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Can change to gpt-4 for better results (higher cost)
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful financial educator. Provide clear, simple explanations about budgeting and personal finance. Never give specific investment advice."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        
        # Extract the response text
        ai_response = response.choices[0].message.content
        
        # Parse and return structured response
        return parse_ai_response(ai_response, budget)
        
    except ValueError as e:
        # API key not set - return demo response
        print(f"AI Service Error: {str(e)}")
        return generate_fallback_response(budget)
        
    except Exception as e:
        # Other errors - log and return fallback
        print(f"AI Service Error: {str(e)}")
        return generate_fallback_response(budget)


def generate_fallback_response(budget: BudgetInput) -> Dict[str, Any]:
    """
    Generate a fallback response when AI is unavailable.
    
    This uses rule-based logic instead of AI.
    
    TODO (Member 3): Improve fallback logic
    """
    # Calculate percentages
    housing_pct = 0
    savings_pct = 0
    
    if budget.monthly_income > 0:
        housing_pct = (budget.expenses.get('rent', 0) / budget.monthly_income) * 100
        savings_pct = (budget.expenses.get('savings', 0) / budget.monthly_income) * 100
    
    # Generate analysis text
    analysis = f"""Based on your monthly income of ${budget.monthly_income:.2f}, here's your budget overview:

Your total expenses are ${budget.total_expenses:.2f}, leaving you with ${budget.remaining:.2f} remaining.

"""
    
    if housing_pct > 30:
        analysis += f"Your housing costs ({housing_pct:.1f}% of income) are above the recommended 30%. This is common in many cities, but consider if there are ways to reduce this expense.\n\n"
    
    if savings_pct < 20:
        analysis += f"You're currently saving {savings_pct:.1f}% of your income. Financial experts often recommend saving 20% if possible. Even small increases can make a big difference over time.\n\n"
    
    analysis += "Remember: The 50/30/20 rule suggests allocating 50% to needs, 30% to wants, and 20% to savings. This is a guideline, not a strict rule - adjust based on your personal situation."
    
    # Calculate breakdown
    breakdown = []
    for category, amount in sorted(
        budget.expenses.items(),
        key=lambda x: x[1],
        reverse=True
    ):
        if budget.monthly_income > 0:
            percentage = (amount / budget.monthly_income) * 100
        else:
            percentage = 0
        breakdown.append({
            'category': category.replace('_', ' ').title(),
            'amount': amount,
            'percentage': round(percentage, 1)
        })
    
    # Generate insights
    insights = []
    
    if budget.monthly_income > 0:
        total_pct = (budget.total_expenses / budget.monthly_income) * 100
        insights.append(f"Your total expenses are {total_pct:.1f}% of your income")
    
    if budget.remaining > 0:
        insights.append(f"You have ${budget.remaining:.2f} unallocated - consider adding this to savings")
    elif budget.remaining < 0:
        insights.append(f"Warning: Your expenses exceed your income by ${abs(budget.remaining):.2f}")
    
    insights.append("Track your spending for a month to see where your money actually goes")
    insights.append("Consider setting up automatic transfers to savings on payday")
    
    return {
        'analysis': analysis,
        'breakdown': breakdown,
        'insights': insights
    }
