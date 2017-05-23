'Computer vision as a Service - Python Client'

from cvas.service_object import ServiceObject
from cvas.util import is_request_success

class Run(ServiceObject):
    """Object Run represents single run of algorithm"""
    def __init__(self, run_id, client=None, json_content=None):
        super(Run, self).__init__(run_id, "/runs", client)
        self.std_out = ""
        self.std_err = ""
        self.status = "notFinished"
        self.duration = 0
        self.file = None
        if json_content is not None:
            self.parse_json(json_content)

    def get(self):
        """Retrieves run info from web service"""
        response = self.client.get_helper(self.get_endpoint())

        if is_request_success(response):
            content = response.json()
            self.parse_json(content)

        return self

    def parse_json(self, json_content):
        """Parse web service response to local object"""
        self.object_id = json_content["id"]
        self.status = json_content["status"]
        if self.status != "notFinished":
            self.std_out = json_content["stdOut"] if "stdOut" in json_content else ""
            self.std_err = json_content["stdErr"] if "stdErr" in json_content else ""
            self.duration = json_content["duration"] if "duration" in json_content else None
            if "file" in json_content:
                self.file = self.client.file(json_content["file"].rsplit('/')[-1])
