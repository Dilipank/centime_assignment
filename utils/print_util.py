from pprint import pprint
from functools import wraps

def pretty_print(msg, indent=2):
    print()
    pprint(msg, indent=indent)


def log_request_response(response):
    print('\n>>>> Request <<<<')
    print(response.request.url)
    print(response.request.headers)
    print('\n>>>> Response <<<<')
    try:
        pretty_print(response.json())
    except Exception:
        pretty_print(response.text)


def logger(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        log_request_response(response)
        return response
    return wrapper
