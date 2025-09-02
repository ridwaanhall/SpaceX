"""
Custom exceptions for the launches app
"""

class APIError(Exception):
    """Custom exception for API errors"""
    pass


class NotFoundError(APIError):
    """Exception for 404 errors"""
    pass


class ValidationError(APIError):
    """Exception for validation errors"""
    pass