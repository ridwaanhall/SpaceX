import base64
import hashlib
import requests
import logging
from cryptography.fernet import Fernet
from django.conf import settings
from .exceptions import APIError, DecryptionError, ValidationError

logger = logging.getLogger(__name__)


def decrypt_url(encrypted_data, key):
    """
    Decrypt the encrypted URL using the provided key.
    """
    try:
        # Create a proper Fernet key from the Django secret key
        hashed_key = hashlib.sha256(key.encode()).digest()
        fernet_key = base64.urlsafe_b64encode(hashed_key)
        
        # Create Fernet cipher
        cipher = Fernet(fernet_key)
        
        # Decrypt the URL
        decrypted_url = cipher.decrypt(encrypted_data.encode())
        
        return decrypted_url.decode()
    
    except Exception as e:
        logger.error(f"URL decryption failed: {str(e)}")
        raise DecryptionError("Failed to decrypt API URL")


def fetch_upcoming_launches():
    """
    Decrypt the upcoming launches API URL and fetch the data.
    """
    encrypted_url = "gAAAAABotdJZNB02tWhl-EeJ_c4nqzsZV2m2paTBK7GNs6MeGyDuUd_83mBfICcDSC65rUraQ_1VOhYwGDbnYiZreqxy_JLUVxf4wcRF7CzuR7-6rZe6lwzaA9VCQpfA10q6HR_HJHtjiF1O4T8tdvmDEn_DutgYaPof252FMXaCMxmLBhriVRU="
    secret_key = settings.SECRET_KEY
    
    try:
        # Decrypt the URL
        decrypted_url = decrypt_url(encrypted_url, secret_key)
        
        # Make the API request with timeout
        response = requests.get(decrypted_url, timeout=30)
        
        # Check for HTTP errors
        if response.status_code == 404:
            raise APIError("Upcoming launches data not found")
        elif response.status_code >= 500:
            raise APIError("SpaceX API is currently unavailable")
        elif response.status_code != 200:
            raise APIError("Failed to retrieve upcoming launches data")
        
        # Validate response content
        try:
            data = response.json()
            if not isinstance(data, list):
                raise ValidationError("Invalid data format received from SpaceX API")
            return data
        except ValueError as e:
            logger.error(f"Invalid JSON response from SpaceX API: {str(e)}")
            raise ValidationError("Invalid response format from SpaceX API")
    
    except DecryptionError:
        raise
    except APIError:
        raise
    except ValidationError:
        raise
    except requests.exceptions.Timeout:
        logger.error("Timeout while fetching upcoming launches data")
        raise APIError("Request timeout - SpaceX API is taking too long to respond")
    except requests.exceptions.ConnectionError:
        logger.error("Connection error while fetching upcoming launches data")
        raise APIError("Unable to connect to SpaceX API")
    except Exception as e:
        logger.error(f"Unexpected error fetching upcoming launches data: {str(e)}")
        raise APIError("An unexpected error occurred while fetching upcoming launches data")
