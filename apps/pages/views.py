from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from apps.crm.models import BlogPost, Testimonial
from .forms import ContactForm
from .models import ContactMessage

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["homepage_promotions"] = BlogPost.objects.filter(
            category="promotion",
            is_published=True,
            show_on_homepage=True,
        ).filter(
            expires_at__isnull=True
        ) | BlogPost.objects.filter(
            category="promotion",
            is_published=True,
            show_on_homepage=True,
            expires_at__gt=timezone.now()
        )

        context["latest_testimonials"] = Testimonial.objects.all()[:3]

        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ContactView(FormView):
    template_name = "pages/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("pages:contact")

    def form_valid(self, form):

        # 1️⃣ Save message to database
        contact = ContactMessage.objects.create(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            phone=form.cleaned_data["phone"],
            message=form.cleaned_data["message"],
        )

        # 2️⃣ Send email notification
        send_mail(
            subject="New Contact Message — Autonecto Electrics",
            message=f"""
New message from Autonecto website:

Name: {contact.name}
Email: {contact.email}
Phone: {contact.phone}

Message:
{contact.message}
""",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["autonectoservices@gmail.com"],
            fail_silently=True,  # prevents crash if email misconfigured
        )

        # 3️⃣ Success message
        messages.success(
            self.request,
            "Your message has been sent successfully!"
        )

        return super().form_valid(form)