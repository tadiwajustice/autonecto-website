from django.db import models
from django.utils import timezone

SERVICE_CHOICES = [
    ("Diagnostics", "Diagnostics"),
    ("Auto Electrical", "Auto Electrical"),
    ("Maintenance", "Maintenance"),
    ("Fleet", "Fleet"),
    ("GPS Tracking", "GPS Tracking"),
    ("Other", "Other"),
]

STATUS_CHOICES = [
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Completed", "Completed"),
]

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100)

    email = models.EmailField()
    phone = models.CharField(max_length=50)

    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    other_service = models.CharField(max_length=100, blank=True, null=True)

    booking_date = models.DateField()
    preferred_time = models.CharField(max_length=50, blank=True, null=True)

    vehicle = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.surname} - {self.service_type}"
