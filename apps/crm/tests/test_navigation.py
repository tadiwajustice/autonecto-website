import pytest

@pytest.mark.django_db
@pytest.mark.parametrize("url", [
    "/",
    "/services/",
    "/contact/",
    "/crm/blog/",
    "/crm/promotions/"
])

def test_navigation_pages(client, url):

    response = client.get(url)

    assert response.status_code == 200