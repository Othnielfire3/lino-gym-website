from decouple import config
import logging

logger = logging.getLogger(__name__)

class Config:
    try:
        SECRET_KEY = config('SECRET_KEY', default='dev-secret-key-change-in-production')
        FLASK_ENV = config('FLASK_ENV', default='development')
        DEBUG = config('FLASK_DEBUG', default=True, cast=bool)
        logger.info("Base configuration loaded successfully")
    except Exception as e:
        logger.error(f"Error loading base configuration: {str(e)}")
        raise

# Resend.com configuration
try:
    RESEND_API_KEY = config('RESEND_API_KEY', default='')
    FROM_EMAIL = config('FROM_EMAIL', default='')
    TO_EMAIL = config('TO_EMAIL', default='')
    CONTACT_SUBJECT = config('CONTACT_SUBJECT', default='New Contact Form Submission - Lino Gym')
    
    # Log configuration status
    logger.info(f"Resend API Key configured: {bool(RESEND_API_KEY)}")
    logger.info(f"From email: {FROM_EMAIL}")
    logger.info(f"To email: {TO_EMAIL}")
    
    if not RESEND_API_KEY:
        logger.warning("RESEND_API_KEY is not set in environment variables")
    if not FROM_EMAIL:
        logger.warning("FROM_EMAIL is not set in environment variables")
    if not TO_EMAIL:
        logger.warning("TO_EMAIL is not set in environment variables")
        
except Exception as e:
    logger.error(f"Error loading email configuration: {str(e)}")
    raise