import pytest
from django.core import mail

@pytest.mark.django_db
def test_contact_form_sends_email(client):

    data = {
        "name": "Test User",
        "email": "test@email.com",
        "phone": "0771234567",
        "message": "Testing email sending"
    }

    client.post("/contact/", data)

    assert len(mail.outbox) == 1
    assert "Testing email sending" in mail.outbox[0].body


@pytest.mark.django_db
def test_contact_form_valid_submission(client):

    data = {
        "name": "Test User",
        "email": "test@email.com",
        "phone": "0771234567",
        "message": "Testing the contact form"
    }

    response = client.post("/contact/", data, follow=True)

    assert response.status_code == 200


@pytest.mark.django_db
def test_contact_form_invalid_email(client):

    data = {
        "name": "Test User",
        "email": "invalid-email",
        "phone": "0771234567",
        "message": "Testing"
    }

    response = client.post("/contact/", data)

    assert response.status_code == 200