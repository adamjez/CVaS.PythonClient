'Computer vision as a Service - Python Client'

from cvas.service_object import ServiceObject
from cvas.util import is_request_success

class Run(ServiceObject):
    """TODO: docstring"""
    def __init__(self, run_id, client=None, json_content=None):
        """TODO: docstring"""
        super(Run, self).__init__(run_id, "/runs", client)
        self.std_out = ""
        self.std_err = ""
        self.status = "notFinished"
        self.duration = 0
        if json_content is not None:
            self.parse_json(json_content)

    def get(self):
        """TODO: docstring"""
        response = self.client.get_helper(self.get_endpoint())

        if is_request_success(response):
            content = response.json()
            self.parse_json(content)

        return self

    def parse_json(self, json_content):
        """TODO: docstring"""
        self.object_id = json_content["id"]
        self.status = json_content["status"]
        if self.status != "notFinished":
            self.std_out = json_content["stdOut"]
            self.std_err = json_content["stdErr"]
            self.duration = json_content["duration"]
