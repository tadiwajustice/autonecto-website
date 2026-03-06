from django import forms
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        min_length=2,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your full name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your email'
        }),
        error_messages={
            'invalid': 'Please enter a valid email address.'
        }
    )

    phone = forms.CharField(
        max_length=13,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'e.g. 0772123456 or +263772123456'
        })
    )

    message = forms.CharField(
        min_length=10,
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Write your message here...'
        })
    )

    # Validate name (letters and spaces only)
    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not re.match(r'^[A-Za-z ]+$', name):
            raise ValidationError("Name should contain only letters and spaces.")

        return name

    # Zimbabwe phone validation
    def clean_phone(self):
        phone = self.cleaned_data.get('phone').strip()

        # Local format: 07XXXXXXXX
        local_pattern = r'^07[1-9][0-9]{7}$'

        # International format: +2637XXXXXXXX
        intl_pattern = r'^\+2637[1-9][0-9]{7}$'

        if re.match(local_pattern, phone):
            # Convert local to international format
            phone = "+263" + phone[1:]
        elif not re.match(intl_pattern, phone):
            raise ValidationError(
                "Enter a valid Zimbabwe phone number "
                "(e.g. 0772123456 or +263772123456)."
            )

        return phone