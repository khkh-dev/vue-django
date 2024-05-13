import pytest
import requests

from app.models import User

from backend.settings.settings import BASE_URL


@pytest.fixture
def user():
    user = User.objects.create(
        first_name="John",
        last_name="Doe",
        email="johndoe@gmail.com",
        username="johndoe",
        about="just John",
    )
    user.set_password("john@doe")
    user.save()
    return user


def test_unauthorized_request():
    url = f"{BASE_URL}/api/users"
    response = requests.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_register_request(api_client, user):
    url = f'{BASE_URL}/api/register'

    data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "janedoe@gmail.com",
        "password": "jane@doe",
        "password_confirm": "jane@doe",
        "username": "janedoe",
        "about": "just Jane",
    }
    response = api_client.post(url, data=data)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["first_name"] == "Jane"
    assert response_body["last_name"] == "Doe"
    assert response_body["email"] == "janedoe@gmail.com"
    assert response_body["about"] == "just Jane"


@pytest.mark.django_db
def test_login_request(api_client, user):
    login_url = f'{BASE_URL}/api/login'

    data = {
        "email": "johndoe@gmail.com",
        "password": "john@doe"
    }
    response = api_client.post(login_url, data=data)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["token"]
    assert isinstance(response_body["token"], str)


@pytest.mark.django_db
def test_logout_request(api_client, user):
    login_url = f'{BASE_URL}/api/login'

    data = {
        "email": "johndoe@gmail.com",
        "password": "john@doe"
    }
    response = api_client.post(login_url, data=data)
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["token"]
    assert isinstance(response_body["token"], str)

    access_token = response_body["token"]
    logout_url = f'{BASE_URL}/api/logout'

    response = api_client.post(logout_url, {}, headers={"Authorization": f"Bearer {access_token}"})
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["message"] == "Successfully logged out"
