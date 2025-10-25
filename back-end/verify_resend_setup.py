import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from decouple import config
import resend

def verify_resend_setup():
    print("=== Resend.com Setup Verification ===")
    
    # Check environment variables
    resend_key = config('RESEND_API_KEY', default='')
    from_email = config('FROM_EMAIL', default='')
    to_email = config('TO_EMAIL', default='')
    
    print(f"RESEND_API_KEY: {'*' * 10 if resend_key else 'NOT SET'}")
    print(f"FROM_EMAIL: {from_email}")
    print(f"TO_EMAIL: {to_email}")
    
    if not resend_key:
        print("❌ RESEND_API_KEY is not set")
        return False
    
    if not from_email:
        print("❌ FROM_EMAIL is not set")
        return False
    
    if not to_email:
        print("❌ TO_EMAIL is not set")
        return False
    
    # Initialize Resend
    resend.api_key = resend_key
    
    # Check if FROM_EMAIL is likely to need domain verification
    if 'gmail.com' in from_email or 'yahoo.com' in from_email or 'hotmail.com' in from_email:
        print("⚠️  WARNING: Using free email provider as FROM_EMAIL")
        print("   You need to verify your domain in Resend dashboard")
        print("   OR use a domain you own and have verified")
        print("   OR use: onboarding@resend.dev for testing")
    
    print("✅ Basic configuration looks good")
    print("\nNext steps:")
    print("1. Go to: https://resend.com/domains")
    print("2. Add and verify your domain")
    print("3. Update FROM_EMAIL in .env to use your verified domain")
    print("4. Or use onboarding@resend.dev for testing")
    
    return True

if __name__ == '__main__':
    verify_resend_setup()