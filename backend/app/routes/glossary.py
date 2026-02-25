"""
============================================
ASSIGNED TO: Member 2 (Backend Lead) & Member 3 (AI/ML Lead)

Glossary API routes - serves financial terms and definitions.

TODO (Member 2):
1. Add search functionality
2. Add pagination for large glossary

TODO (Member 3):
1. Add AI-powered term explanation endpoint
2. Expand the glossary with more terms
============================================
"""

from flask import Blueprint, request, jsonify

glossary_bp = Blueprint('glossary', __name__)

# Financial glossary data
# TODO (Member 3): Review and expand this list
GLOSSARY_TERMS = [
    {
        'id': 1,
        'term': 'Budget',
        'definition': 'A plan that helps you track your income and expenses over a specific period.',
        'category': 'basics'
    },
    {
        'id': 2,
        'term': 'Stock',
        'definition': 'A share of ownership in a company.',
        'category': 'investing'
    },
    {
        'id': 3,
        'term': 'ETF',
        'definition': 'Exchange-Traded Fund - a basket of multiple stocks or bonds that you can buy as a single investment.',
        'category': 'investing'
    },
    {
        'id': 4,
        'term': 'Bond',
        'definition': 'A loan you give to a company or government in exchange for regular interest payments.',
        'category': 'investing'
    },
    {
        'id': 5,
        'term': 'Risk',
        'definition': 'The possibility of losing some or all of your investment.',
        'category': 'investing'
    },
    {
        'id': 6,
        'term': 'Diversification',
        'definition': 'Spreading your investments across different types of assets to reduce risk.',
        'category': 'investing'
    },
    {
        'id': 7,
        'term': 'Compound Interest',
        'definition': 'Interest earned on both your original money AND the interest already added.',
        'category': 'basics'
    },
    {
        'id': 8,
        'term': 'Emergency Fund',
        'definition': 'Money set aside for unexpected expenses (3-6 months of living expenses recommended).',
        'category': 'basics'
    },
    {
        'id': 9,
        'term': '50/30/20 Rule',
        'definition': 'Budgeting guideline: 50% needs, 30% wants, 20% savings.',
        'category': 'basics'
    },
    {
        'id': 10,
        'term': 'Inflation',
        'definition': 'The gradual increase in prices over time, reducing purchasing power.',
        'category': 'economics'
    },
]

@glossary_bp.route('/glossary', methods=['GET'])
def get_glossary():
    """
    Get all glossary terms.
    Optional query params:
    - category: Filter by category (basics, investing, economics)
    - search: Search term in name or definition
    """
    category = request.args.get('category')
    search = request.args.get('search', '').lower()
    
    terms = GLOSSARY_TERMS
    
    # Filter by category
    if category:
        terms = [t for t in terms if t['category'] == category]
    
    # Filter by search term
    if search:
        terms = [t for t in terms if 
                 search in t['term'].lower() or 
                 search in t['definition'].lower()]
    
    return jsonify({
        'terms': terms,
        'count': len(terms)
    }), 200


@glossary_bp.route('/glossary/<int:term_id>', methods=['GET'])
def get_term(term_id):
    """Get a specific glossary term by ID."""
    term = next((t for t in GLOSSARY_TERMS if t['id'] == term_id), None)
    
    if not term:
        return jsonify({
            'error': 'Not found',
            'message': f'Term with ID {term_id} not found'
        }), 404
    
    return jsonify(term), 200


@glossary_bp.route('/glossary/explain', methods=['POST'])
def explain_term():
    """
    Get an AI-powered explanation of a financial term using Gemini.

    Expected JSON body:
    {
        "term": "ETF",
        "complexity": "beginner"  // beginner, intermediate, advanced
    }
    """
    # Import here to avoid circular imports at module load time
    from app.services.ai_service import get_gemini_client, GEMINI_AVAILABLE

    if not GEMINI_AVAILABLE:
        return jsonify({
            'error': 'unavailable',
            'message': 'AI explanations are currently unavailable.'
        }), 503

    data = request.get_json() or {}
    term = (data.get('term') or '').strip()
    complexity = (data.get('complexity') or 'beginner').lower()
    custom_prompt = (data.get('custom_prompt') or '').strip()

    if not term:
        return jsonify({
            'error': 'invalid_request',
            'message': 'term is required'
        }), 400

    if complexity not in ['beginner', 'intermediate', 'advanced']:
        complexity = 'beginner'

    # Try to find a base glossary definition
    base_def = next(
        (t for t in GLOSSARY_TERMS if t['term'].lower() == term.lower()),
        None,
    )
    base_text = base_def['definition'] if base_def else ''

    try:
        # Try AI first; if it fails, we'll fall back to rule-based explanation below
        client = get_gemini_client()

        if custom_prompt:
            # User provided a custom prompt/question
            prompt = f"""The user is asking about the financial term "{term}".

Existing definition (if helpful): {base_text}

User's specific question/request: {custom_prompt}

Answer their question clearly and simply. Use 2-4 short paragraphs. Include examples if helpful. Do NOT recommend specific investments or products.
"""
        else:
            # Standard explanation
            prompt = f"""Explain the financial term "{term}" for a {complexity} learner.

Existing definition (if helpful): {base_text}

Rules:
- Use 2-3 short paragraphs max.
- Use simple, friendly language.
- Include ONE concrete example.
- Do NOT recommend specific investments or products.

Format:
- First paragraph: simple explanation.
- Second paragraph: example.
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            config={
                "max_output_tokens": 400,
                "temperature": 0.5,
            },
        )
        text = response.text or ""

        return jsonify({
            'term': term,
            'complexity': complexity,
            'explanation': text.strip(),
        }), 200

    except Exception as e:
        # Log for debugging, but don't break the UI
        print(f"Glossary AI explanation error (fallback to rule-based): {type(e).__name__}: {e}")

    # Rule-based fallback explanation when AI fails
    if base_text:
        explanation = f"Here is a simple explanation of {term}:\n\n{base_text}\n\n"
        if custom_prompt:
            explanation += f"In the context of your question (“{custom_prompt}”), think of {term} this way: {base_text}"
    else:
        explanation = f"{term} is a financial term. At the moment we don't have a detailed definition stored, but it usually refers to a concept used in investing or budgeting."

    return jsonify({
        'term': term,
        'complexity': complexity,
        'explanation': explanation,
    }), 200
