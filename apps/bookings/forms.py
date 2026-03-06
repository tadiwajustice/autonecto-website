from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
                "first_name",
                "second_name",
                "surname",
                "email",
                "phone",
                "service_type",
                "other_service",
                "vehicle",
                "preferred_time",
                "booking_date",
                "message",
                "notes",
            ]

        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
