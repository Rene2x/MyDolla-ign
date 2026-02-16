"""
============================================
ASSIGNED TO: Member 2 (Backend Lead)

Main Flask application entry point.

TODO:
1. Add proper error handling middleware
2. Add request logging
3. Add rate limiting for API endpoints
4. Set up proper CORS configuration for production
============================================
"""

import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import routes
from app.routes.budget import budget_bp
from app.routes.glossary import glossary_bp

def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Enable CORS for frontend communication
    # TODO (Member 2): Configure this properly for production
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Register blueprints (route modules)
    app.register_blueprint(budget_bp, url_prefix='/api')
    app.register_blueprint(glossary_bp, url_prefix='/api')
    
    # Health check endpoint
    @app.route('/api/health')
    def health_check():
        return {'status': 'healthy', 'service': 'My Dolla $ign API'}
    
    return app

# Create the Flask application
app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"Starting My Dolla $ign API server on port {port}")
    print(f"Health check: http://localhost:{port}/api/health")
    print(f"Budget analysis: POST http://localhost:{port}/api/analyze")
    
    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=port,
        debug=debug
    )
