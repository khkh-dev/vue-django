import json
import os
import sqlite3

import pytest
import requests

from django.urls import reverse

from rest_framework.test import APIClient

from app.models import User
from django.test import Client
from rest_framework.test import APIClient

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


@pytest.mark.django_db
def test_get_user(api_client, user):
    login_url = f'{BASE_URL}/api/login'
    users_url = f'{BASE_URL}/api/users/'

    response = api_client.post(login_url, data={
        "email": "johndoe@gmail.com",
        "password": "john@doe"
    })
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["token"]
    assert isinstance(response_body["token"], str)

    access_token = response_body["token"]
    response = api_client.get(users_url, headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200

    response_body = response.json()
    assert isinstance(response_body, dict)

    assert response_body["id"]
    assert response_body["first_name"]
    assert response_body["last_name"]
    assert response_body["email"]
    assert response_body["username"]
    assert response_body["about"]

    assert response_body["id"] == user.id
    assert response_body["first_name"] == user.first_name
    assert response_body["last_name"] == user.last_name
    assert response_body["email"] == user.email
    assert response_body["username"] == user.username
    assert response_body["about"] == user.about


@pytest.mark.django_db
def test_update_user(api_client, user):
    login_url = f'{BASE_URL}/api/login'
    update_user_url = f'{BASE_URL}/api/users/{user.id}/'

    response = api_client.post(login_url, data={
        "email": "johndoe@gmail.com",
        "password": "john@doe"
    })
    response_body = response.json()

    assert response.status_code == 200
    assert response_body["token"]
    assert isinstance(response_body["token"], str)

    access_token = response_body["token"]
    response = api_client.patch(
        path=update_user_url,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
        format="json",
        data={
            "first_name": "Johnny",
            "last_name": "Dude",
            "email": "cool89john@gmail.com",
            "username": "cool89john",
            "about": "just a Johnny",
        }
    )
    response_body = response.json()
    assert response_body["id"]
    assert response_body["first_name"]
    assert response_body["last_name"]
    assert response_body["email"]
    assert response_body["username"]
    assert response_body["about"]

    assert response.status_code == 200
    assert response_body["id"] == user.id
    assert response_body["first_name"] == "Johnny"
    assert response_body["last_name"] == "Dude"
    assert response_body["email"] == "cool89john@gmail.com"
    assert response_body["username"] == "cool89john"
    assert response_body["about"] == "just a Johnny"
