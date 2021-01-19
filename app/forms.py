from django import forms
from django.core.exceptions import ValidationError
import re


def phone_validator(value):
    if re.match(r'^\+?\d{11}$', value) is None:
        raise ValidationError(message='Номер телефона должен быть в формате +12345678912 или 12345678912')


class MailForm(forms.Form):
    email = forms.EmailField(label='Email')
    name = forms.CharField(max_length=50, label='Your name')
    phone = forms.CharField(validators=[phone_validator], label='Phone', required=False)
    text = forms.CharField(widget=forms.Textarea, required=False)

    email.widget.attrs.update({'class': 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    phone.widget.attrs.update({'class': 'form-control'})
    text.widget.attrs.update({'class': 'form-control'})
