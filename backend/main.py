import os
import json
from pathlib import Path
from flask import Flask, render_template, request
from flask_cors import CORS
from dotenv import load_dotenv

# Load backend/.env no matter which directory you run `python main.py` from
_BACKEND_DIR = Path(__file__).resolve().parent
load_dotenv(_BACKEND_DIR / ".env")

from app.services.ai_service import analyze_budget
from app.models.budget import BudgetInput, validate_budget_input

from app.routes.budget import budget_bp
from app.routes.glossary import glossary_bp


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(budget_bp, url_prefix='/api')
    app.register_blueprint(glossary_bp, url_prefix='/api')

    @app.route('/', methods=['GET'])
    def home():
        return render_template(
            'index.html',
            monthly_income="",
            expenses="",
            info="",
            explanation="",
            quiz="",
            tip=""
        )

    @app.route('/analyze', methods=['POST'])
    def analyze_form():
        monthly_income = request.form.get('monthly_income', '')
        expenses = request.form.get('expenses', '')
        info = request.form.get('info', '')

        explanation = ""
        quiz = ""
        tip = ""

        try:
            data = {
                'monthly_income': float(monthly_income),
                'expenses': json.loads(expenses),
                'goal': info if info else 'general'
            }

            validation_result = validate_budget_input(data)

            if not validation_result['valid']:
                explanation = validation_result['message']
            else:
                budget_input = BudgetInput(
                    monthly_income=data['monthly_income'],
                    expenses=data['expenses'],
                    goal=data['goal']
                )

                result = analyze_budget(budget_input)

                explanation = result.get('analysis') or result.get('financial_advice') or 'No explanation available.'
                tip = result.get('financial_advice') or 'No financial tip available.'
                quiz = "What does the 50/30/20 rule suggest you do with 20% of your income?"

        except json.JSONDecodeError:
            explanation = 'Expenses must be valid JSON using double quotes, for example: {"rent": 1000, "food": 400}'
        except ValueError:
            explanation = 'Income must be a number.'
        except Exception as e:
            print(f"Error in /analyze route: {e}")
            explanation = 'An error occurred while analyzing your budget.'

        return render_template(
            'index.html',
            monthly_income=monthly_income,
            expenses=expenses,
            info=info,
            explanation=explanation,
            quiz=quiz,
            tip=tip
        )

    @app.route('/api/health')
    def health_check():
        from app.services.ai_service import GENAI_STUDIO_AVAILABLE, VERTEX_AVAILABLE

        key_set = bool(os.getenv("GEMINI_API_KEY", "").strip())
        project_set = bool(os.getenv("GOOGLE_CLOUD_PROJECT", "").strip())
        return {
            "status": "healthy",
            "service": "My Dolla $ign API",
            "ai": {
                "google_generativeai_installed": GENAI_STUDIO_AVAILABLE,
                "vertex_sdk_installed": VERTEX_AVAILABLE,
                "gemini_api_key_set": key_set,
                "google_cloud_project_set": project_set,
                "hint": (
                    "Install: pip install -r requirements.txt; set GEMINI_API_KEY in backend/.env"
                    if not GENAI_STUDIO_AVAILABLE
                    else "Set GEMINI_API_KEY in backend/.env"
                    if not key_set
                    else "OK for Google AI Studio"
                ),
            },
        }

    return app


app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    print(f"Starting My Dolla $ign API server on port {port}")
    print(f"Health check: http://localhost:{port}/api/health")
    print(f"Budget analysis: POST http://localhost:{port}/api/analyze")
    print(f"Quiz grading: POST http://localhost:{port}/api/grade-quiz")

    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=port,
        debug=debug
    )