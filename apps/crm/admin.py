from django.contrib import admin
from .models import BlogPost, Testimonial, Promotion


# 🔹 BLOG POSTS
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_published",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "category",
        "is_published",
        "is_featured",
    )

    search_fields = ("title", "content")

    prepopulated_fields = {"slug": ("title",)}

    ordering = ("-created_at",)

    fieldsets = (
        ("Content", {
            "fields": ("title", "slug", "category", "excerpt", "content", "image")
        }),
        ("Publishing", {
            "fields": ("is_published", "is_featured"),
        }),
    )


# 🔥 PROMOTIONS (Separate Admin Section)
@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "expires_at",
        "show_on_homepage",
        "is_published",
        "created_at",
    )

    list_filter = (
        "is_published",
        "show_on_homepage",
    )

    search_fields = ("title", "content")

    prepopulated_fields = {"slug": ("title",)}

    ordering = ("-created_at",)

    fieldsets = (
        ("Content", {
            "fields": ("title", "slug", "excerpt", "content", "image")
        }),
        ("Promotion Settings", {
            "fields": ("expires_at", "show_on_homepage"),
        }),
        ("Publishing", {
            "fields": ("is_published",),
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(category="promotion")

    def save_model(self, request, obj, form, change):
        obj.category = "promotion"
        super().save_model(request, obj, form, change)


# 🔹 TESTIMONIALS
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = ("name", "company", "rating", "created_at")

    list_filter = ("rating",)

    search_fields = ("name", "message")

    ordering = ("-created_at",)