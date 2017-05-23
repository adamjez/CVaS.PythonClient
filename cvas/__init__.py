'Computer vision as a Service - Python Client'

from cvas.client import Client

import os

apiKey = None
apiEndpoint = None

def client(api_key=None, api_address=None):
    """Creates client with given api_key and api_address"""
    return Client(api_key, api_address)


defaultClient = None

def getDefaultClient():
    """Creates default client"""
    global defaultClient
    # Check for default client, and ensure default API key has not changed
    if defaultClient is None or defaultClient.apiKey is not apiKey:
        # Construct default client
        defaultClient = Client(apiKey, apiEndpoint)
    return defaultClient

def getApiAddress():
    """Get api address from env var or default value"""
    if 'CVAS_API_ENDPOINT' in os.environ:
        # Then check for system environment variable
        return os.environ['CVAS_API_ENDPOINT']
    else:
        # Else return default
        return "http://localhost:4485"
