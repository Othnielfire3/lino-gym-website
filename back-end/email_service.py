import resend
from decouple import config
from flask import flash
import logging
import sys

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('email_service.log')
    ]
)

logger = logging.getLogger(__name__)

class EmailService:
    def __init__(self):
        try:
            self.resend_api_key = config('RESEND_API_KEY')
            self.from_email = config('FROM_EMAIL')
            self.to_email = config('TO_EMAIL')
            self.contact_subject = config('CONTACT_SUBJECT')
            
            # Initialize Resend with API key
            resend.api_key = self.resend_api_key
            
            logger.info("EmailService initialized successfully")
            logger.info(f"From email: {self.from_email}")
            logger.info(f"To email: {self.to_email}")
            logger.info(f"Resend API key present: {bool(self.resend_api_key)}")
            
        except Exception as e:
            logger.error(f"Failed to initialize EmailService: {str(e)}")
            raise

    def send_contact_email(self, name, email, phone, message):
        """Send contact form submission via Resend.com"""
        logger.info(f"Attempting to send contact email from {name} ({email})")
        
        try:
            # Validate required fields
            if not all([name, email, message]):
                error_msg = "Missing required fields: name, email, or message"
                logger.error(error_msg)
                return False, error_msg

            # Format the email content
            html_body = f"""
            <h2>New Contact Form Submission - Lino Gym</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Phone:</strong> {phone if phone else 'Not provided'}</p>
            <h3>Message:</h3>
            <p>{message}</p>
            <hr>
            <p><em>Sent from Lino Gym Contact Form</em></p>
            """
            
            text_body = f"""
            New Contact Form Submission - Lino Gym
            
            Name: {name}
            Email: {email}
            Phone: {phone if phone else 'Not provided'}
            
            Message:
            {message}
            """
            
            params = {
                "from": self.from_email,
                "to": [self.to_email],
                "subject": self.contact_subject,
                "html": html_body,
                "text": text_body
            }
            
            logger.debug(f"Email parameters: { {k: v for k, v in params.items() if k != 'text' and k != 'html'} }")
            
            # Send email
            logger.info("Sending email via Resend API...")
            email_response = resend.Emails.send(params)
            logger.info(f"Email sent successfully! Response: {email_response}")
            
            return True, "Thank you for your message! We will get back to you soon."
            
        except resend.core.ResendError as e:
            error_msg = f"Resend API error: {str(e)}"
            logger.error(error_msg)
            logger.error(f"Error type: {type(e).__name__}")
            return False, "Sorry, there was an error with our email service. Please try again later."
            
        except Exception as e:
            error_msg = f"Unexpected error sending email: {str(e)}"
            logger.error(error_msg)
            logger.error(f"Error type: {type(e).__name__}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            return False, "Sorry, there was an unexpected error. Please try again later."

# Create a global instance
try:
    email_service = EmailService()
    logger.info("Email service instance created successfully")
except Exception as e:
    logger.error(f"Failed to create EmailService instance: {str(e)}")
    email_service = None