from django.urls import path
from .views import BlogListView, BlogDetailView, PromotionsView, TestimonialsView

app_name = "crm"

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    path("promotions/", PromotionsView.as_view(), name="promotions"),
    path("testimonials/", TestimonialsView.as_view(), name="testimonials"),
]