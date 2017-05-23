'Computer vision as a Service - Python Client'

import json
import requests

import cvas
from cvas.run import Run
from cvas.algorithm import Algorithm
from cvas.file import File
from cvas.util import is_request_success

class Client(object):
    """Represents client for communication with web service at given endpoint"""
    def __init__(self, api_key, api_endpoint=None):
        self.api_key = api_key
        self.api_endpoint = api_endpoint if api_endpoint is not None else cvas.getApiAddress()

    def run(self, run_id):
        """Shortcut for creating run"""
        return Run(run_id, self).get()

    def algorithm(self, code_name):
        """Shortcut for creating algorithm"""
        return Algorithm(code_name, self)

    def all_algorithms(self):
        response = self.get_helper("/algorithms")

        algorithms = []
        if is_request_success(response):
            content = response.json()
            for alg in content:
                algorithms.append(self.algorithm(alg["codeName"]))
        else:
            None

        return algorithms

    def file(self, file_id):
        """Shortcut for creating run"""
        return File(file_id, self)

    def upload_file(self, path):
        """Shortcut for uploading file"""
        return File(None, self).upload(path)

    def upload_data(self, data, content_type, extension):
        """Shortcut for uploading data in memory"""
        return File(None, self).upload_from_data(data, content_type, extension)

    def append_basic_headers(self, headers):
        """Creates basic HTTP headers for all requests"""
        headers = headers if headers is not None else {}

        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'
        if 'Authorization' not in headers and self.api_key is not None:
            headers['Authorization'] = "Simple " + self.api_key

        return headers

    def get_helper(self, url_segments, headers=None, **query_parameters):
        """HTTP GET request"""
        headers = self.append_basic_headers(headers)
        response = requests.get(self.api_endpoint + url_segments, headers=headers,
                                params=query_parameters)
        return response

    def post_helper(self, url_segments, input_object, headers=None, **query_parameters):
        """HTTP POST request"""
        headers = self.append_basic_headers(headers)
        input_json = json.dumps(input_object).encode('utf-8')
        headers['Content-Type'] = 'application/json'
        return requests.post(self.api_endpoint + url_segments, data=input_json,
                             headers=headers, params=query_parameters)

    def post_file_helper(self, url_segments, multipart_form_data, headers=None, **query_parameters):
        """HTTP POST request with multipart_form_data for files"""
        headers = self.append_basic_headers(headers)
        return requests.post(self.api_endpoint + url_segments, files=multipart_form_data,
                             headers=headers, params=query_parameters)

    def delete_helper(self, url_segments, headers=None, **query_parameters):
        """HTTP DELETE request"""
        headers = self.append_basic_headers(headers)
        return requests.delete(self.api_endpoint + url_segments, headers=headers,
                               params=query_parameters)
