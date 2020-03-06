import logging
import pytest
from pytest_socket import disable_socket


def pytest_runtest_setup():
    disable_socket()


LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def example_fixture():
    LOGGER.info("Setting Up Example Fixture...")
    yield
    LOGGER.info("Tearing Down Example Fixture...")
