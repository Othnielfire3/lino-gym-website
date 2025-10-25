from flask import Flask
from decouple import config as decouple_config
import os
import sys
import logging

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import Config

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('flask_app.log')
    ]
)

logger = logging.getLogger(__name__)

def create_app():
    """Application factory pattern"""
    # Get the root directory (one level up from back-end)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    app = Flask(__name__,
                template_folder=root_dir,  # Templates are in root directory
                static_folder=root_dir)    # Static files are in root directory
    
    # Load configuration
    app.config.from_object(Config)
    
    # Log startup information
    logger.info("Flask app starting up...")
    logger.info(f"Template folder: {app.template_folder}")
    logger.info(f"Static folder: {app.static_folder}")
    logger.info(f"Debug mode: {app.config['DEBUG']}")
    
    # Import and initialize routes
    try:
        from routes import init_routes
        init_routes(app)
        logger.info("Routes initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize routes: {str(e)}")
        raise
    
    return app

if __name__ == '__main__':
    app = create_app()
    logger.info("Starting Flask application on http://localhost:5000")
    app.run(debug=app.config['DEBUG'], port=5000)