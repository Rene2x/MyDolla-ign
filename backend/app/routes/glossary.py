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
    Get an AI-powered explanation of a financial term.
    
    TODO (Member 3): Implement AI-powered explanations
    
    Expected JSON body:
    {
        "term": "ETF",
        "complexity": "beginner"  // beginner, intermediate, advanced
    }
    """
    # TODO (Member 3): Implement this endpoint
    return jsonify({
        'message': 'AI explanation endpoint - coming soon!',
        'status': 'not_implemented'
    }), 501
