import os
from pathlib import Path

from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

_BACKEND_DIR = Path(__file__).resolve().parent
load_dotenv(_BACKEND_DIR / ".env")

from app.routes.budget import budget_bp
from app.routes.glossary import glossary_bp


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.register_blueprint(budget_bp, url_prefix='/api')
    app.register_blueprint(glossary_bp, url_prefix='/api')

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({
            "service": "My Dolla $ign API",
            "health": "/api/health",
            "analyze": "POST /api/analyze",
            "grade_quiz": "POST /api/grade-quiz",
        })

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
