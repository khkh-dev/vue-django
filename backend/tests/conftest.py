import pytest

from rest_framework.test import APIClient

from django.conf import settings


# def pytest_configure():
#     settings.configure(DATABASES="db.sqlite3")


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    """
    Fixture to provide an API client
    :return: APIClient
    """
    yield APIClient()
