from dataclasses import dataclass


@dataclass
class UserServiceConfig:
    """Defining the service configurations"""
    ENV: str

    def __post_init__(self):
        self.base_endpoint = {
            'local': 'http://localhost...',  # placeholder for local route
            'remote': 'https://farpve1134.execute-api.us-east-1.amazonaws.com'
        }[self.ENV]
