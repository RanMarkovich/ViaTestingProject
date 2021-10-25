from pytest import mark

from tests.test_utils import validate_response_error


def test_create_user_returns_status_code_200(user_data_factory, user_test_helper):
    """
    1. Calls create user
    2. Asserts status code 200
    """
    user_creation_payload = user_data_factory.create_user_payload()
    r = user_test_helper.create_user(user_creation_payload)
    assert r.status_code == 200, validate_response_error(r, payload=user_creation_payload)


def test_create_user_response_with_valid_payload(user_data_factory, user_test_helper):
    """
    1. Calls create user
    2. Asserts valid response payload
    """
    user_creation_payload = user_data_factory.create_user_payload()
    r = user_test_helper.create_user(user_creation_payload)
    u_id = r.json()['data']['id']
    assert r.json() == user_data_factory.expected_user_creation_resp_payload(user_creation_payload, u_id)


@mark.parametrize('invalid_payload', [('first_name', ''), ('last_name', ''), ('age', None), ('email', '')])
def test_err_when_trying_to_create_user_with_invalid_value(invalid_payload, user_data_factory, user_test_helper):
    """
    1. Calls create user with invalid payload (each test serves different invalid field)
    2. Asserts 400 bad request status code
    """
    field_name, invalid_value = invalid_payload
    user_creation_payload = user_data_factory.create_user_payload()
    user_creation_payload[field_name] = invalid_value
    r = user_test_helper.create_user(user_creation_payload)
    assert r.status_code == 400, validate_response_error(r, 400, user_creation_payload)
