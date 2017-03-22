'Computer vision as a Service - Python Client'

def success_status_code(status_code):
    return status_code >= 200 and status_code <= 299

def is_request_success(request):
    if success_status_code(request.status_code):
        return True
    if 'isError' in request:
        raise Exception(request['message'])
    else:
        raise Exception(request.status_code)

