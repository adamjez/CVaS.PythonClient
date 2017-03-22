'Computer vision as a Service - Python Client'

import tempfile

from cvas.service_object import ServiceObject
from cvas.util import is_request_success
import cvas.make_json_serializable

class File(ServiceObject):
    """TODO: docstring"""
    def __init__(self, file_id=None, client=None):
        """TODO: docstring"""
        super(File, self).__init__(file_id, "/files", client)

    def download(self):
        """TODO: docstring"""
        if id is None:
            raise Exception('file does not exist')
        # Make HTTP get request
        response = self.client.get_helper(self.get_endpoint())
        if is_request_success(response):
            with tempfile.NamedTemporaryFile(delete=False) as file:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    file.write(block)
                file.flush()
                return open(file.name)
        return None

    def upload(self, path):
        """Post file to data api"""
        multipart_form_data = {'file': open(path, 'rb')}
        response = self.client.post_file_helper(self.url_segments, multipart_form_data)
        if is_request_success(response):
            self.object_id = response.json()['ids'][0]
        return self

    def delete(self):
        """Delete from data api"""
        result = self.client.delete_helper(self.get_endpoint())
        return is_request_success(result)

    def to_json(self):
        """TODO: docstring"""
        return "local://" + str(self.object_id)
