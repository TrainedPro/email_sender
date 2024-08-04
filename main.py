import yagmail
import logging
import os
import re
import sys
from dotenv import load_dotenv
from argparse import ArgumentParser

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Default values (can be edited directly in the script)
DEFAULT_RECIPIENT_EMAIL = ""
DEFAULT_SUBJECT = ""
DEFAULT_BODY = ""
DEFAULT_ATTACHMENT_PATH = ""  # Leave empty if no attachment

def is_valid_email(email):
    """Validate email address format."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def send_certificate(email, subject=None, body=None, attachment_path=None, sender_email=None, sender_password=None):
    try:
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=email,
            subject=subject or 'No Subject',
            contents=body or '',
            attachments=attachment_path if attachment_path else []
        )
        logger.info(f"Email sent to {email} successfully.")
    except Exception as e:
        logger.error(f"Failed to send email to {email}. Error: {str(e)}")

def main():
    # Set up argument parser
    parser = ArgumentParser(description="Send an email with an optional attachment.")
    parser.add_argument("-r", "--recipient", help="Recipient email address")
    parser.add_argument("-s", "--subject", help="Email subject")
    parser.add_argument("-b", "--body", help="Email body (text or HTML)")
    parser.add_argument("-a", "--attachment", help="Path to attachment")
    
    args = parser.parse_args()
    
    # Environment variables
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    # Use command-line arguments or default values
    recipient_email = args.recipient or DEFAULT_RECIPIENT_EMAIL
    subject = args.subject or DEFAULT_SUBJECT
    body = args.body or DEFAULT_BODY
    attachment_path = args.attachment or DEFAULT_ATTACHMENT_PATH
    
    if not sender_email or not sender_password:
        logger.error("Sender email and sender password must be set in the .env file.")
        sys.exit(1)
    
    if not is_valid_email(recipient_email):
        logger.error(f"Invalid recipient email address: {recipient_email}")
        sys.exit(1)

    send_certificate(
        email=recipient_email,
        subject=subject,
        body=body,
        attachment_path=attachment_path,
        sender_email=sender_email,
        sender_password=sender_password
    )

if __name__ == "__main__":
    main()
