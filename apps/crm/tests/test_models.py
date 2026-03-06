import pytest
from apps.crm.models import BlogPost


@pytest.mark.django_db
def test_blog_post_creation():

    post = BlogPost.objects.create(
        title="Test Blog",
        content="Test content"
    )

    assert post.title == "Test Blog"
    
    
@pytest.mark.django_db
def test_blog_detail_page(client):

    post = BlogPost.objects.create(
        title="Test Post",
        content="Test content"
    )

    response = client.get(f"/crm/blog/{post.id}/")

    assert response.status_code == 200