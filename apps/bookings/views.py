from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages

from .models import Booking
from .forms import BookingForm


# -----------------------------
# ADMIN-ONLY BOOKING LIST VIEW
# -----------------------------
class BookingListView(UserPassesTestMixin, ListView):
    model = Booking
    template_name = "bookings/booking_list.html"
    context_object_name = "bookings"
    ordering = ["-created_at"]

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect("pages:home")


# -----------------------------
# PUBLIC BOOKING FORM VIEW
# -----------------------------
class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = "bookings/booking_form.html"
    success_url = reverse_lazy("bookings:booking_thankyou")

    def form_valid(self, form):
        messages.success(self.request, "Your booking has been submitted successfully!")
        return super().form_valid(form)


# -----------------------------
# THANK YOU PAGE
# -----------------------------
class BookingThankYouView(TemplateView):
    template_name = "bookings/booking_thankyou.html"
