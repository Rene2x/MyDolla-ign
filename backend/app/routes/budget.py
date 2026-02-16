"""
============================================
ASSIGNED TO: Member 2 (Backend Lead)

Budget API routes - handles budget analysis requests.

TODO:
1. Add input validation
2. Add error handling for edge cases
3. Add request rate limiting
4. Add caching for repeated requests (optional)
============================================
"""

from flask import Blueprint, request, jsonify
from app.services.ai_service import analyze_budget
from app.models.budget import BudgetInput, validate_budget_input

budget_bp = Blueprint('budget', __name__)

@budget_bp.route('/analyze', methods=['POST'])
def analyze_budget_endpoint():
    """
    Analyze a user's budget and return AI-generated insights.
    
    Expected JSON body:
    {
        "monthly_income": 3000,
        "expenses": {
            "rent": 1200,
            "food": 400,
            "transportation": 150,
            "utilities": 100,
            "entertainment": 200,
            "savings": 300,
            "other": 150
        }
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'error': 'No data provided',
                'message': 'Please provide budget data in JSON format'
            }), 400
        
        # Validate input
        # TODO (Member 2): Improve validation with Pydantic
        validation_result = validate_budget_input(data)
        if not validation_result['valid']:
            return jsonify({
                'error': 'Invalid input',
                'message': validation_result['message']
            }), 400
        
        # Create BudgetInput object
        budget_input = BudgetInput(
            monthly_income=data.get('monthly_income', 0),
            expenses=data.get('expenses', {})
        )
        
        # Call AI service to analyze the budget
        # TODO (Member 3): This is where AI integration happens
        result = analyze_budget(budget_input)
        
        return jsonify(result), 200
        
    except Exception as e:
        # TODO (Member 2): Add proper logging here
        print(f"Error analyzing budget: {str(e)}")
        return jsonify({
            'error': 'Analysis failed',
            'message': 'An error occurred while analyzing your budget. Please try again.'
        }), 500


@budget_bp.route('/analyze/demo', methods=['GET'])
def demo_analysis():
    """
    Returns a demo analysis with sample data.
    Useful for testing the frontend without AI API calls.
    """
    demo_result = {
        'analysis': """Based on your monthly income of $3,000, here's your budget breakdown:

You're spending 40% of your income on housing ($1,200), which is slightly above the recommended 30% guideline. Consider this the area with the most potential for savings if possible.

Your food expenses at $400 (13%) are reasonable for a single person. Great job keeping this in check!

You're saving $300 per month (10%), which is a good start! The general recommendation is to save at least 20% of your income. Consider gradually increasing this as you find ways to reduce other expenses.""",
        
        'breakdown': [
            {'category': 'Rent/Housing', 'amount': 1200, 'percentage': 40},
            {'category': 'Food/Groceries', 'amount': 400, 'percentage': 13.3},
            {'category': 'Savings', 'amount': 300, 'percentage': 10},
            {'category': 'Entertainment', 'amount': 200, 'percentage': 6.7},
            {'category': 'Transportation', 'amount': 150, 'percentage': 5},
            {'category': 'Other', 'amount': 150, 'percentage': 5},
            {'category': 'Utilities', 'amount': 100, 'percentage': 3.3},
        ],
        
        'insights': [
            'Your housing costs are 40% of income - aim for 30% or less if possible',
            'You\'re saving 10% - try to increase to 20% over time',
            'Consider the 50/30/20 rule: 50% needs, 30% wants, 20% savings',
            'Great job tracking your expenses! Awareness is the first step to better finances'
        ]
    }
    
    return jsonify(demo_result), 200
