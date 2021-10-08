from pprint import pprint


def pretty_print(msg, indent=2):
    print()
    pprint(msg, indent=indent)

def log_request_response(response):
    print('\n>>>> Request <<<<')
    print(response.request.url)
    print(response.request.headers)
    print('>>>> Response <<<<')
    pretty_print(response.json())