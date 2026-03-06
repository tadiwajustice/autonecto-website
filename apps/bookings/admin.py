from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "surname",
        "phone",
        "service_type",
        "status",
        "booking_date",
        "created_at",
    )

    list_filter = (
        "status",
        "service_type",
        "booking_date",
    )

    search_fields = (
        "first_name",
        "surname",
        "phone",
        "vehicle",
    )

    ordering = ("-created_at",)

    list_editable = ("status",)
