import pytest

@pytest.mark.django_db
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_services_page(client):
    response = client.get("/services/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_contact_page(client):
    response = client.get("/contact/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_blog_page(client):
    response = client.get("/crm/blog/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_promotions_page(client):
    response = client.get("/crm/promotions/")
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_404_page(client):

    response = client.get("/nonexistent-page/")

    assert response.status_code == 404