from flask import render_template, request, redirect, url_for, flash, session
from email_service import email_service
import os
import logging

logger = logging.getLogger(__name__)

def init_routes(app):
    """Initialize all routes for the application"""
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/class')
    def class_page():
        return render_template('class.html')
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            # Get form data from the existing form
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            
            logger.info(f"Contact form submitted - Name: {name}, Email: {email}, Phone: {phone}")
            
            # Basic validation
            if not all([name, email, message]):
                flash('Please fill in all required fields: Name, Email, and Message.', 'error')
                logger.warning("Form validation failed - missing required fields")
                return render_template('contact.html')
            
            # Check if email service is available
            if email_service is None:
                error_msg = "Email service is not available. Please check configuration."
                logger.error(error_msg)
                flash('Our email service is currently unavailable. Please try again later.', 'error')
                return render_template('contact.html')
            
            # Send email
            try:
                success, message_result = email_service.send_contact_email(
                    name=name,
                    email=email,
                    phone=phone,
                    message=message
                )
                
                if success:
                    flash(message_result, 'success')
                    logger.info(f"Contact form processed successfully for {email}")
                else:
                    flash(message_result, 'error')
                    logger.error(f"Contact form failed for {email}: {message_result}")
                
            except Exception as e:
                error_msg = f"Unexpected error in contact route: {str(e)}"
                logger.error(error_msg)
                import traceback
                logger.error(f"Traceback: {traceback.format_exc()}")
                flash('An unexpected error occurred. Please try again later.', 'error')
            
            return redirect(url_for('contact'))
        
        return render_template('contact.html')
    
    @app.route('/feature')
    def feature():
        return render_template('feature.html')