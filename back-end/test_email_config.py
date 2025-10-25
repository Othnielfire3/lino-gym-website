import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from decouple import config

def test_config():
    print("=== Testing Email Configuration ===")
    
    # Test environment variables
    resend_key = config('RESEND_API_KEY', default='NOT_SET')
    from_email = config('FROM_EMAIL', default='NOT_SET')
    to_email = config('TO_EMAIL', default='NOT_SET')
    
    print(f"RESEND_API_KEY: {'*' * 10 if resend_key != 'NOT_SET' else 'NOT_SET'}")
    print(f"FROM_EMAIL: {from_email}")
    print(f"TO_EMAIL: {to_email}")
    
    if resend_key == 'NOT_SET':
        print("❌ RESEND_API_KEY is not set in .env file")
    else:
        print("✅ RESEND_API_KEY is set")
    
    if from_email == 'NOT_SET':
        print("❌ FROM_EMAIL is not set in .env file")
    else:
        print("✅ FROM_EMAIL is set")
    
    if to_email == 'NOT_SET':
        print("❌ TO_EMAIL is not set in .env file")
    else:
        print("✅ TO_EMAIL is set")

if __name__ == '__main__':
    test_config()