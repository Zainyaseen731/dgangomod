from django.core.exceptions import ValidationError

def valid_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("NOt a valid email")