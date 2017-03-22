'Computer vision as a Service - Python Client'

from cvas.client import Client

import os

apiKey = None
apiEndpoint = None

def client(api_key=None, api_address=None):
    """TODO: docstring"""
    return Client(api_key, api_address)


defaultClient = None

def getDefaultClient():
    """TODO: docstring"""
    global defaultClient
    # Check for default client, and ensure default API key has not changed
    if defaultClient is None or defaultClient.apiKey is not apiKey:
        # Construct default client
        defaultClient = Client(apiKey, apiEndpoint)
    return defaultClient

def getApiAddress():
    """TODO: docstring"""
    if 'CVAS_API_ENDPOINT' in os.environ:
        # Then check for system environment variable
        return os.environ['CVAS_API_ENDPOINT']
    else:
        # Else return default
        return "http://localhost:4485"
