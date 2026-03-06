from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

from .models import BlogPost, Testimonial
from .forms import TestimonialForm


# 🔥 BLOG LIST
class BlogListView(ListView):
    model = BlogPost
    template_name = "crm/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return BlogPost.objects.filter(
            is_published=True
        ).exclude(category="promotion")


# 🔥 BLOG DETAIL
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "crm/blog_detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"


# 🔥 PROMOTIONS (Auto-hide expired)
class PromotionsView(ListView):
    model = BlogPost
    template_name = "crm/promotions.html"
    context_object_name = "promotions"

    def get_queryset(self):
        now = timezone.now()

        return BlogPost.objects.filter(
            category="promotion",
            is_published=True
        ).filter(
            Q(expires_at__isnull=True) |
            Q(expires_at__gt=now)
        )


# 🔥 TESTIMONIALS
class TestimonialsView(ListView):
    model = Testimonial
    template_name = "crm/testimonials.html"
    context_object_name = "testimonials"

    def get_queryset(self):
        return Testimonial.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TestimonialForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TestimonialForm(request.POST)

        if form.is_valid():
            testimonial = form.save()

            send_mail(
                subject="New Testimonial Submitted - Autonecto",
                message=f"""
New testimonial submitted:

Name: {testimonial.name}
Company: {testimonial.company}
Rating: {testimonial.rating} stars

Message:
{testimonial.message}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["autonectoservices@gmail.com"],
                fail_silently=True,
            )

        return redirect("crm:testimonials")