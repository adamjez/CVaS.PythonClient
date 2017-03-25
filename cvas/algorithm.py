'Computer vision as a Service - Python Client'

from cvas.service_object import ServiceObject
from cvas.util import is_request_success
from cvas.run import Run

class Algorithm(ServiceObject):
    """TODO: docstring"""
    def __init__(self, code_name=None, client=None):
        """TODO: docstring"""
        super(Algorithm, self).__init__(code_name, "/algorithms", client)

    def run(self, arguments=None, timeout=-1):
        """TODO: docstring"""
        endpoint_with_timeout = self.get_endpoint() + "?timeout=" + str(timeout)
        response = self.client.post_helper(endpoint_with_timeout, arguments)

        if is_request_success(response):
            content = response.json()
            return Run(content["id"], self.client, content)
        return None
