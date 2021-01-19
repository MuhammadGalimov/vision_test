from django import forms


class MailForm(forms.Form):
    email = forms.EmailField(label='Email')
    name = forms.CharField(max_length=50, label='Your name')
    phone = forms.RegexField(regex=r'^\+?\d{11}$',
                             error_messages="Номер телефона должен быть в формате +99999999999 или 99999999999",
                             label='Phone number', required=False)
    text = forms.CharField(widget=forms.Textarea, required=False)
