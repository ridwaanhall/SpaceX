"""
Custom exceptions for the upcoming app
"""

class APIError(Exception):
    """Raised when external API call fails or returns error"""
    pass

class DecryptionError(Exception):
    """Raised when URL decryption fails"""
    pass

class ValidationError(Exception):
    """Raised when data validation fails"""
    pass
