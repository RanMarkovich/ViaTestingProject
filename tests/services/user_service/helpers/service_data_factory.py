from copy import deepcopy
from dataclasses import dataclass

from tests.common_fucntions import load_json_file, random_string_generator, random_integer_generator


@dataclass
class UserDataFactory:
    """Responsible for all payload manipulations before initializing a request to service"""

    __create_user_payload = load_json_file('user_service/data/user_creation_payload.json')
    __exp_user_creation_resp_payload = load_json_file('user_service/data/user_creation_resp_payload.json')

    def create_user_payload(self, f_name: str = '', l_name: str = '', age: int = 0, email: str = ''):
        payload = deepcopy(self.__create_user_payload)
        payload['first_name'] = f_name if f_name else random_string_generator()
        payload['last_name'] = l_name if l_name else random_string_generator()
        payload['age'] = age if age else random_integer_generator()
        payload['email'] = email if email else random_string_generator() + '@fakemail.com'
        return payload

    def expected_user_creation_resp_payload(self, user_payload: dict, u_id: str, is_success: bool = True):
        payload = deepcopy(self.__exp_user_creation_resp_payload)
        payload['success'] = is_success
        user_payload.update({'id': u_id})
        payload.update({'data': user_payload})
        return payload
