import time
from config import wait_time
from utils.errors import throttling_error


def handle_throttle(f):
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        if 'throttle_ignore' in kwargs and not kwargs['throttle_ignore']:
            return response
        if throttling_error.strip() in response.text:
            time.sleep(wait_time)
            return f(*args, **kwargs)
        return response
    return wrapper
