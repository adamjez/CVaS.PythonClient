'Computer vision as a Service - Python Client'

import tempfile

from cvas.service_object import ServiceObject
from cvas.util import is_request_success
import cvas.make_json_serializable

class File(ServiceObject):
    """File represents uploaded file or result of algorithm run"""
    def __init__(self, file_id=None, client=None):
        super(File, self).__init__(file_id, "/files", client)
        self.content_type = None

    def downloadAndOpen(self):
        """Downloads file from web service and return it opened"""
        if self.object_id is None:
            raise Exception('file does not exist')
        # Make HTTP get request
        response = self.client.get_helper(self.get_endpoint())
        if is_request_success(response):
            self.content_type = response.headers['Content-Type']
            with tempfile.NamedTemporaryFile(delete=False) as file:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    file.write(block)
                file.flush()
                return open(file.name)
        return None

    def download(self, file_name):
        """Downloads file from web service """
        if self.object_id is None:
            raise Exception('file does not exist')
        # Make HTTP get request
        response = self.client.get_helper(self.get_endpoint())
        if is_request_success(response):
            self.content_type = response.headers['Content-Type']
            with open(file_name, "wb") as file:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    file.write(block)
                file.flush()
                return True
        return False

    def upload(self, path_to_file):
        """Post file to data api"""
        multipart_form_data = {'file': open(path_to_file, 'rb')}
        return self.__upload(multipart_form_data)

    def upload_from_data(self, data, content_type, extension):
        """Post file to data api"""
        multipart_form_data = {'file': (extension, data, content_type)}
        return self.__upload(multipart_form_data)

    def __upload(self, multipart_form_data):
        response = self.client.post_file_helper(self.url_segments, multipart_form_data)
        data = response.json()
        if is_request_success(response) and len(data) > 0:
            self.object_id = data[0]['id']
        return self
        
    def delete(self):
        """Delete from data api"""
        result = self.client.delete_helper(self.get_endpoint())
        return is_request_success(result)

    def to_json(self):
        return "local://" + str(self.object_id)
