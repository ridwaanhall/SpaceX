import base64
import hashlib
import requests
from cryptography.fernet import Fernet
from django.conf import settings


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
    
    except Exception as e:
        raise Exception(f"Error fetching launches data: {str(e)}")
