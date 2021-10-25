from dataclasses import dataclass

import requests

from tests.services.user_service.config import UserServiceConfig


@dataclass
class UserServiceTestHelper:
    """Implementation of all the service endpoints"""
    Config: UserServiceConfig

    def __post_init__(self):
        self.base_endpoint = self.Config.base_endpoint
        self.api_endpoint = f"{self.base_endpoint}/api"
        self.create_user_api = f"{self.api_endpoint}/CreateUser"

    def create_user(self, payload: dict):
        r = requests.post(self.create_user_api, json=payload)
        return r
