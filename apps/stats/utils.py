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


def fetch_spacex_data():
    """
    Decrypt the SpaceX API URL and fetch the data.
    """
    encrypted_url = "gAAAAABotc_VnohHocfLezez5cPjv1PfU5GhcpZfItTAxHEaseyd5svgvZGZlwmuBAtlICiAaVGqLZmVqQNwCi_Dq43UqrwCELpWVY1K9ZwhxS7kIYA_5R8ijoHru1-IPE0mFJosjiC_QZqsRatVvlv0zHcoqpLFm2sroOciihWCrO_eiYO5fKY="
    secret_key = settings.SECRET_KEY
    
    try:
        # Decrypt the URL
        decrypted_url = decrypt_url(encrypted_url, secret_key)
        
        # Make the API request with timeout
        response = requests.get(decrypted_url, timeout=30)
        
        # Check for HTTP errors
        if response.status_code == 404:
            raise APIError("SpaceX stats data not found")
        elif response.status_code >= 500:
            raise APIError("SpaceX API is currently unavailable")
        elif response.status_code != 200:
            raise APIError("Failed to retrieve SpaceX stats data")
        
        # Validate response content
        try:
            data = response.json()
            if not isinstance(data, dict):
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
        logger.error("Timeout while fetching SpaceX stats data")
        raise APIError("Request timeout - SpaceX API is taking too long to respond")
    except requests.exceptions.ConnectionError:
        logger.error("Connection error while fetching SpaceX stats data")
        raise APIError("Unable to connect to SpaceX API")
    except Exception as e:
        logger.error(f"Unexpected error fetching SpaceX stats data: {str(e)}")
        raise APIError("An unexpected error occurred while fetching SpaceX data")
