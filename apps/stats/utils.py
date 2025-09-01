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


def fetch_spacex_data():
    """
    Decrypt the SpaceX API URL and fetch the data.
    """
    encrypted_url = "gAAAAABotc_VnohHocfLezez5cPjv1PfU5GhcpZfItTAxHEaseyd5svgvZGZlwmuBAtlICiAaVGqLZmVqQNwCi_Dq43UqrwCELpWVY1K9ZwhxS7kIYA_5R8ijoHru1-IPE0mFJosjiC_QZqsRatVvlv0zHcoqpLFm2sroOciihWCrO_eiYO5fKY="
    secret_key = settings.SECRET_KEY
    
    try:
        # Decrypt the URL
        decrypted_url = decrypt_url(encrypted_url, secret_key)
        
        # Make the API request
        response = requests.get(decrypted_url, timeout=30)
        response.raise_for_status()
        
        return response.json()
    
    except Exception as e:
        raise Exception(f"Error fetching SpaceX data: {str(e)}")
