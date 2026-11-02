import re
from email_validator import validate_email, EmailNotValidError

def validate_realistic_email(email_input: str) -> str:
    """
    Validates that an email address:
    1. Has valid syntax and active DNS MX records (deliverability check).
    2. Is not from a disposable/burner email domain.
    3. Conforms to provider-specific length and character constraints (e.g., Gmail 6-30 chars).
    """
    if not email_input:
        raise ValueError("Email address is required.")

    email_str = str(email_input).strip()

    try:
        # 1. DNS deliverability check (MX record resolution)
        val = validate_email(email_str, check_deliverability=True)
        domain = val.domain.lower()
        local_part = val.local_part.lower()

        # 2. Block disposable/temporary burner email providers
        disposable_domains = {
            'mailinator.com', 'tempmail.com', '10minutemail.com',
            'guerrillamail.com', 'trashmail.com', 'yopmail.com',
            'throwawaymail.com', 'sharklasers.com', 'getairmail.com'
        }
        if domain in disposable_domains:
            raise ValueError(f"Disposable/temporary email addresses from '{domain}' are not allowed.")

        # 3. Provider-specific constraints
        if domain in {'gmail.com', 'googlemail.com'}:
            clean_user = local_part.replace('.', '')
            if len(clean_user) < 6:
                raise ValueError("Invalid Gmail address: Username must be at least 6 characters long.")
            if len(clean_user) > 30:
                raise ValueError("Invalid Gmail address: Gmail usernames cannot exceed 30 characters.")
            if not re.match(r'^[a-z0-9.]+$', local_part):
                raise ValueError("Invalid Gmail address: Only letters, numbers, and periods are permitted.")

        return val.normalized

    except EmailNotValidError as e:
        raise ValueError(f"Email address or domain is invalid/undeliverable: {str(e)}")
