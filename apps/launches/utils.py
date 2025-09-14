import base64
import hashlib
import requests
from cryptography.fernet import Fernet
from django.conf import settings
import logging
from datetime import datetime, time, date
from .exceptions import APIError, NotFoundError, ValidationError

logger = logging.getLogger(__name__)


def decrypt_url(encrypted_data, key):
    """
    Decrypt the encrypted URL using the provided key.
    """
    # Create a proper Fernet key from the Django secret key
    hashed_key = hashlib.sha256(key.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(hashed_key)
    
    # Create Fernet cipher
    cipher = Fernet(fernet_key)
    
    # Decrypt the URL
    decrypted_url = cipher.decrypt(encrypted_data.encode())
    
    return decrypted_url.decode()


def fetch_launches_data():
    """
    Decrypt the launches API URL and fetch the data.
    """
    encrypted_url = "gAAAAABotdgnMa5IuX_1uk7RhNLrojiAhUigJo_lfJt8izk6hZ-Huc92Kr3P57udOx1dJ3bHyfbCXmUpWfNi-sSF6BPfgfnZ5pRnabt6eVn7cnA7NsvaNmeCVUl-KKDdsGGJGZpa6TUWhxPXPdVkLfq00UvLf-TpsVacm0nj4aaMVmH1vIYXKnw="
    secret_key = settings.SECRET_KEY
    
    try:
        # Decrypt the URL
        decrypted_url = decrypt_url(encrypted_url, secret_key)
        
        # Make the API request
        response = requests.get(decrypted_url, timeout=30)
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.Timeout:
        logger.error("Timeout occurred while fetching launches data")
        raise APIError("Service temporarily unavailable. Please try again later.")
    
    except requests.exceptions.ConnectionError:
        logger.error("Connection error occurred while fetching launches data")
        raise APIError("Unable to connect to data source. Please try again later.")
    
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred while fetching launches data: {e.response.status_code}")
        if e.response.status_code == 404:
            raise NotFoundError("Launches data not found.")
        elif e.response.status_code >= 500:
            raise APIError("External service error. Please try again later.")
        else:
            raise APIError("Failed to retrieve launches data.")
    
    except Exception as e:
        logger.error(f"Unexpected error fetching launches data: {str(e)}")
        raise APIError("An unexpected error occurred. Please try again later.")


def fetch_launch_detail(link):
    """
    Decrypt the launch detail API URL and fetch specific launch data using the link parameter.
    """
    # Validate link parameter to prevent injection
    if not link or not isinstance(link, str) or len(link) > 100:
        raise ValidationError("Invalid launch identifier provided.")
    
    # Basic sanitization
    import re
    if not re.match(r'^[a-zA-Z0-9\-_]+$', link):
        raise ValidationError("Launch identifier contains invalid characters.")
    
    encrypted_detail_url = "gAAAAABotqX39erTnt50rCjm_vpcCHhSGOvx1mBL9AtkHHEyKssHQaqPtbwc8lZ7E759sdrfDcLioYi9NjgRGfYaQ3Xp3JJimaIMPD_XCX15pCubNz6hW3SCAfq-5y3mXPbKUgqknG-nTlLrCKp_yatbWynvVuTdcw=="
    secret_key = settings.SECRET_KEY
    
    try:
        # Decrypt the base URL
        decrypted_base_url = decrypt_url(encrypted_detail_url, secret_key)
        
        # Construct the full URL with the link parameter
        detail_url = f"{decrypted_base_url}/{link}"
        
        # Make the API request
        response = requests.get(detail_url, timeout=30)
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.Timeout:
        logger.error(f"Timeout occurred while fetching launch detail for link: {link}")
        raise APIError("Service temporarily unavailable. Please try again later.")
    
    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error occurred while fetching launch detail for link: {link}")
        raise APIError("Unable to connect to data source. Please try again later.")
    
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred while fetching launch detail for link {link}: {e.response.status_code}")
        if e.response.status_code == 404:
            raise NotFoundError("Launch not found. Please check the launch identifier and try again.")
        elif e.response.status_code >= 500:
            raise APIError("External service error. Please try again later.")
        else:
            raise APIError("Failed to retrieve launch details.")
    
    except Exception as e:
        logger.error(f"Unexpected error fetching launch detail for link {link}: {str(e)}")
        raise APIError("An unexpected error occurred. Please try again later.")


def sort_launches_by_datetime(launches_data):
    """
    Sort launches by datetime (combining launchDate and launchTime) with latest first.
    
    Args:
        launches_data: List of launch dictionaries containing launchDate and launchTime
        
    Returns:
        Sorted list with latest launches first (descending order)
    """
    def get_launch_datetime(launch):
        """Extract and combine launch date and time for sorting"""
        try:
            launch_date = launch.get('launchDate')
            launch_time = launch.get('launchTime')
            
            # Handle different possible date formats
            if isinstance(launch_date, str):
                # Try to parse string date
                try:
                    parsed_date = datetime.strptime(launch_date, '%Y-%m-%d').date()
                except ValueError:
                    try:
                        parsed_date = datetime.strptime(launch_date, '%m/%d/%Y').date()
                    except ValueError:
                        # If we can't parse the date, put it at the end
                        return datetime.min
            elif isinstance(launch_date, date):
                parsed_date = launch_date
            else:
                # If no valid date, put at the end
                return datetime.min
            
            # Handle time
            if isinstance(launch_time, str):
                # Try to parse string time
                try:
                    parsed_time = datetime.strptime(launch_time, '%H:%M:%S').time()
                except ValueError:
                    try:
                        parsed_time = datetime.strptime(launch_time, '%H:%M').time()
                    except ValueError:
                        # If we can't parse time, use midnight
                        parsed_time = time(0, 0)
            elif isinstance(launch_time, time):
                parsed_time = launch_time
            else:
                # If no valid time, use midnight
                parsed_time = time(0, 0)
            
            # Combine date and time
            return datetime.combine(parsed_date, parsed_time)
            
        except Exception as e:
            logger.warning(f"Error parsing launch datetime: {str(e)}")
            # Return minimum datetime for problematic entries
            return datetime.min
    
    try:
        # Sort by datetime in descending order (latest first)
        sorted_launches = sorted(launches_data, key=get_launch_datetime, reverse=True)
        return sorted_launches
    except Exception as e:
        logger.error(f"Error sorting launches by datetime: {str(e)}")
        # Return original data if sorting fails
        return launches_data
