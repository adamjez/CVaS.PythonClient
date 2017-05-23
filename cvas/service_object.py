'Computer vision as a Service - Python Client'

import cvas

class ServiceObject(object):
    """Service object is base class for web services objects"""
    def __init__(self, object_id, url_segments, client):
        self.client = client if client is not None else cvas.getDefaultClient()
        self.url_segments = url_segments
        self.object_id = object_id

    def get_endpoint(self):
        """Creates endpoint with url_segments and object_id"""
        return self.url_segments + '/' + str(self.object_id)
