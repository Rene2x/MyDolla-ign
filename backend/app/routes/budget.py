"""
Budget API routes — POST /api/analyze (budget JSON) and POST /api/grade-quiz (quiz grading JSON).

Teammate task (documentation): keep README, docs/milestone2_demo.md, and docs/prompt_design.md aligned
with these two endpoints and the three-step UI (quiz, AI verdict, then explanation and tip).
"""
import json
from flask import Blueprint, request, jsonify
from app.services.ai_service import analyze_budget, grade_quiz_answer
from app.models.budget import BudgetInput, validate_budget_input

budget_bp = Blueprint('budget', __name__)


def _parse_budget_payload():
    """Accept JSON (React) or multipart form (legacy)."""
    data = request.get_json(silent=True)
    if data is not None and isinstance(data, dict):
        return data, None
    if request.form:
        try:
            raw = request.form.to_dict()
            if 'expenses' in raw and isinstance(raw['expenses'], str):
                raw['expenses'] = json.loads(raw['expenses'])
            raw['monthly_income'] = float(raw.get('monthly_income', 0))
            return raw, None
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            return None, str(e)
    return None, None


@budget_bp.route('/analyze', methods=['POST'])
def analyze_budget_endpoint():
    """
    Analyze a user's budget. Frontend sends JSON:
    {
        "monthly_income": 3000,
        "expenses": { "rent": 1200, ... },
        "goal": "general"
    }
    """
    try:
        data, form_err = _parse_budget_payload()
        if data is None:
            msg = (
                'Send JSON: {"monthly_income": number, "expenses": {...}, "goal": "general"}'
                if form_err is None
                else f'Invalid form data: {form_err}'
            )
            return jsonify({'error': 'Invalid request', 'message': msg}), 400

        if not data:
            return jsonify({
                'error': 'No data provided',
                'message': 'Please provide budget data as JSON'
            }), 400

        validation_result = validate_budget_input(data)
        if not validation_result['valid']:
            return jsonify({
                'error': 'Invalid input',
                'message': validation_result['message']
            }), 400

        budget_input = BudgetInput(
            monthly_income=float(data.get('monthly_income', 0)),
            expenses=data.get('expenses', {}),
            goal=data.get('goal', 'general')
        )

        result = analyze_budget(budget_input)
        return jsonify(result), 200

    except Exception as e:
        print(f"Error analyzing budget: {str(e)}")
        return jsonify({
            'error': 'Analysis failed',
            'message': 'An error occurred while analyzing your budget. Please try again.'
        }), 500


@budget_bp.route('/grade-quiz', methods=['POST'])
def grade_quiz_endpoint():
    """
    Grade the user's quiz answer (AI, same credentials as analyze).

    JSON body:
    {
        "quiz_question": "...",
        "quiz_answer_key": "...",
        "user_answer": "..."
    }
    """
    try:
        data = request.get_json(silent=True)
        if not isinstance(data, dict):
            return jsonify({'error': 'Invalid request', 'message': 'Send JSON body'}), 400

        q = (data.get('quiz_question') or '').strip()
        key = (data.get('quiz_answer_key') or '').strip()
        ans = (data.get('user_answer') or '').strip()

        if not q:
            return jsonify({'error': 'Invalid input', 'message': 'quiz_question is required'}), 400
        if not ans:
            return jsonify({
                'error': 'Invalid input',
                'message': 'Please enter an answer before submitting for grading.',
            }), 400

        result = grade_quiz_answer(q, key, ans)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({'error': 'Invalid input', 'message': str(e)}), 400
    except Exception as e:
        print(f"Error grading quiz: {e}")
        return jsonify({
            'error': 'Grading failed',
            'message': 'Could not grade this answer. Please try again.',
        }), 500


@budget_bp.route('/analyze/demo', methods=['GET'])
def demo_analysis():
    """
    Returns a demo analysis with sample data.
    Useful for testing the frontend without AI API calls.
    """
    demo_result = {
        'analysis': 'Demo analysis text (see financial_advice, quiz_question, grounded_tip).',
        'financial_advice': (
            "Based on your monthly income of $3,000, housing is $1,200 (40% of income)—above the "
            "30% housing guideline in our rules. You allocate $300 (10%) to savings; the Savings "
            "Benchmarks rule recommends working toward 15–20% over time."
        ),
        'quiz_question': (
            "Given your income of $3,000 and savings of $300 per month (10% of income), what does the "
            "Savings Benchmarks rule in our docs consider the minimum, recommended, and strong savings "
            "rates as a percentage of income?"
        ),
        'quiz_answer_key': (
            "A solid answer names your 10% ($300 of $3,000) rate and ties it to Savings Benchmarks: "
            "about 10% as a floor, roughly 15–20% as a recommended range, and 20%+ as strong."
        ),
        'grounded_tip': (
            "Per the Emergency Fund Guideline (docs/financial_rules.md), aim to hold 3–6 months of "
            "essential expenses in cash. With about $2,700/month in expenses in this sample budget, a "
            "minimum emergency fund target would be roughly $8,100."
        ),
        'grounded_rule_citation': 'Emergency Fund Guideline; Savings Benchmarks; Housing 30% guideline',
        'output_source': 'demo_static',
        'saving_tips': [
            'You have $500 left after expenses—consider directing part to savings.',
        ],
        'saving_plan': {
            'months_1_3': [
                'Increase savings from 10% to 12% of income',
                'Set up automatic transfer of $100/month to emergency fund',
                'Build emergency fund: aim for $1,000 first'
            ],
            'months_4_6': [
                'Grow savings to 15% of income',
                'Increase emergency fund to 2 months of expenses',
                'Review and optimize housing costs if possible'
            ]
        },
        'where_savings_could_go': (
            "After an emergency fund, people often learn about high-yield savings accounts, "
            "employer retirement accounts (401(k)), IRAs, and broad market index funds. "
            "Talk to a licensed financial advisor for your situation."
        ),
        'goal': 'general',
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
            'Your housing costs are 40% of income — aim for 30% or less if possible',
            "You're saving 10% — try to increase to 20% over time",
            '50/30/20 rule: 50% needs, 30% wants, 20% savings',
            'Awareness is the first step to better finances',
        ],
    }
    return jsonify(demo_result), 200
