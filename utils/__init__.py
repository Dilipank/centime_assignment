import time
from config import wait_time


def handle_throttle(f):
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception:
            time.sleep(wait_time)
        return wrapper
    return handle_throttle
