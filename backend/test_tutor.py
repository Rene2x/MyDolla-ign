#!/usr/bin/env python3
"""
Terminal test script for AI Tutor.
Run: python test_tutor.py

Make sure you have:
1. Set GEMINI_API_KEY in your .env file (get it from https://aistudio.google.com/apikey)
"""

import json
import os
import sys

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from src.ai_tutor import AITutor

def print_section(title: str, content: str):
    """Pretty print a section."""
    print(f"\n{'='*60}")
    print(f" {title}")
    print('='*60)
    print(content)

def main():
    print("\n" + "="*60)
    print(" MY DOLLA $IGN - AI BUDGET TUTOR TEST")
    print("="*60)
    
    # Check environment
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\nERROR: GEMINI_API_KEY not set!")
        print("1. Go to https://aistudio.google.com/apikey")
        print("2. Create an API key")
        print("3. Add to backend/.env: GEMINI_API_KEY=your-key")
        return
    
    print(f"\nUsing Gemini API (key: ...{api_key[-8:]})")
    
    # Sample user budget data
    user_data = {
        "monthly_income": 4000,
        "total_expenses": 3500,
        "remaining": 500,
        "goal": "emergency_fund",
        "expenses": {
            "rent": 1400,        # 35% - high
            "food": 500,         # 12.5%
            "transportation": 300,  # 7.5%
            "utilities": 150,    # 3.75%
            "entertainment": 400,   # 10%
            "savings": 400,      # 10% - below recommended
            "other": 350,        # 8.75%
        }
    }
    
    print("\n--- USER BUDGET DATA ---")
    print(f"Monthly Income: ${user_data['monthly_income']}")
    print(f"Total Expenses: ${user_data['total_expenses']}")
    print(f"Remaining: ${user_data['remaining']}")
    print(f"Goal: {user_data['goal']}")
    print("\nExpenses:")
    for category, amount in user_data['expenses'].items():
        pct = (amount / user_data['monthly_income']) * 100
        print(f"  - {category.title()}: ${amount} ({pct:.1f}%)")
    
    print("\n--- CALLING AI TUTOR ---")
    print("(This may take a few seconds...)\n")
    
    try:
        tutor = AITutor()
        result = tutor.generate_session(user_data)
        
        # Display results
        print_section("STATUS", result.get("status", "unknown"))
        
        print_section("EXPLANATION", result.get("explanation", "No explanation"))
        
        quiz = result.get("quiz", {})
        quiz_text = f"Question: {quiz.get('question', 'N/A')}\n\nAnswer: {quiz.get('answer', 'N/A')}\n\nRules Referenced: {quiz.get('rule_ids', [])}"
        print_section("QUIZ", quiz_text)
        
        tip = result.get("tip", {})
        tip_text = f"{tip.get('text', 'N/A')}\n\nRules Referenced: {tip.get('rule_ids', [])}"
        print_section("TIP", tip_text)
        
        print_section("RULES USED", str(result.get("used_rule_ids", [])))
        
        print("\n" + "="*60)
        print(" FULL JSON RESPONSE")
        print("="*60)
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
