from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):

    CATEGORY_CHOICES = [
        ("tips", "Tips"),
        ("promotion", "Promotion"),
        ("announcement", "Announcement"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    excerpt = models.TextField(blank=True)
    content = models.TextField()

    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="tips"
    )

    # 🔥 Promotion Features
    expires_at = models.DateTimeField(blank=True, null=True)
    show_on_homepage = models.BooleanField(default=False)

    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# 🔥 Proxy Model (creates separate Promotions section in Admin)
class Promotion(BlogPost):
    class Meta:
        proxy = True
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"


class Testimonial(models.Model):

    RATING_CHOICES = [
        (5, "★★★★★"),
        (4, "★★★★"),
        (3, "★★★"),
        (2, "★★"),
        (1, "★"),
    ]

    name = models.CharField(max_length=150)
    message = models.TextField()

    company = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=150, blank=True)

    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name