from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "company", "position", "rating", "message"]

        widgets = {
            "message": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Share your experience..."
            }),
            "name": forms.TextInput(attrs={
                "placeholder": "Your Name"
            }),
            "company": forms.TextInput(attrs={
                "placeholder": "Company (optional)"
            }),
            "position": forms.TextInput(attrs={
                "placeholder": "Position (optional)"
            }),
        }