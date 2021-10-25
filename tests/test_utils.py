from requests import Response


def validate_response_error(r: Response, status_code: int = 200, payload: dict = None):
    return f"Test Failed! Expected to get status code {status_code}, " \
           f"sent {r.request.method} request to endpoint: {r.url}, with payload:{payload} and got: {r.text}"
