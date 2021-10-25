from pytest import fixture

from tests.services.user_service.config import UserServiceConfig
from tests.services.user_service.helpers.service_data_factory import UserDataFactory
from tests.services.user_service.helpers.service_test_helper import UserServiceTestHelper


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="remote",
        help="env: local or remote"
    )


@fixture
def env(request):
    return request.config.getoption("--env")


@fixture
def user_service_conf(env):
    return UserServiceConfig(env)


@fixture
def user_test_helper(user_service_conf):
    return UserServiceTestHelper(user_service_conf)


@fixture
def user_data_factory():
    return UserDataFactory()
