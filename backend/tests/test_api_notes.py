import pytest

from app.models import User, Note

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


@pytest.fixture
def notes(user):
    notes = Note.objects.bulk_create(
        [
            Note(title="title", text="lorem ipsum dolor sit amet", user=user),
            Note(title="title", text="lorem ipsum dolor sit amet", user=user),
            Note(title="title", text="lorem ipsum dolor sit amet", user=user),
            Note(title="title", text="lorem ipsum dolor sit amet", user=user),
            Note(title="title", text="lorem ipsum dolor sit amet", user=user),
        ]
    )
    return notes


@pytest.fixture
def token(api_client, user):
    login_url = f'{BASE_URL}/api/login'

    response = api_client.post(login_url, data={
        "email": "johndoe@gmail.com",
        "password": "john@doe"
    })
    response_body = response.json()
    return response_body["token"]


@pytest.mark.django_db
def test_list_notes(api_client, token, notes):
    notes_url = f'{BASE_URL}/api/notes/'

    response = api_client.get(notes_url, headers={"Authorization": f"Bearer {token}"})
    response_body = response.json()

    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert len(response_body) == 5

    for _, note in enumerate(response_body):
        note_id = _ + 1
        assert note["id"] == note_id
        assert note["title"] == "title"
        assert note["text"] == "lorem ipsum dolor sit amet"


@pytest.mark.django_db
def test_create_note(api_client, token, user):
    create_note_url = f'{BASE_URL}/api/notes/'

    response = api_client.post(
        path=create_note_url,
        headers={
            "Authorization": f"Bearer {token}",
        },
        format="json",
        data={
            "title": "a new note's title",
            "text": "a new note's text",
            "user": user.id
        }
    )
    response_body = response.json()
    assert isinstance(response_body, dict)

    created_note = Note.objects.last()

    assert response_body["id"] == created_note.id
    assert response_body["title"] == created_note.title
    assert response_body["text"] == created_note.text


@pytest.mark.django_db
def test_update_note(api_client, token, notes):
    update_note_url = f'{BASE_URL}/api/notes/{notes[0].id}/'

    response = api_client.patch(
        path=update_note_url,
        headers={
            "Authorization": f"Bearer {token}",
        },
        format="json",
        data={
            "title": "updated title",
            "text": "updated text"
        }
    )
    response_body = response.json()
    assert isinstance(response_body, dict)

    updated_note = Note.objects.get(id=notes[0].id)

    assert response_body["id"] == updated_note.id
    assert response_body["title"] == updated_note.title
    assert response_body["text"] == updated_note.text


@pytest.mark.django_db
def test_delete_note(api_client, token, notes):
    delete_note_url = f'{BASE_URL}/api/notes/{notes[0].id}/'

    response = api_client.delete(
        path=delete_note_url,
        headers={
            "Authorization": f"Bearer {token}",
        },
        format="json",
        data={}
    )

    assert response.status_code == 204
    assert len(Note.objects.all()) == 4


@pytest.mark.django_db
def test_detail_note(api_client, token, notes):
    detail_note_url = f'{BASE_URL}/api/notes/{notes[0].id}/'

    # TODO: ADD LOGIN FIXTURE TO USE IN TEST CASES
    # TODO: ADD TEST CASES TO REFRESH TOKEN, TO EXPIRE IT MANUALLY AND TO CHECK LOGIN

    response = api_client.get(
        path=detail_note_url,
        headers={
            "Authorization": f"Bearer {token}",
        },
        format="json",
        data={}
    )
    response_body = response.json()
    assert response.status_code == 200
    assert isinstance(response_body, dict)
