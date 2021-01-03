from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50, required=True)
    email_address = forms.EmailField(required=True)
    subject = forms.CharField(max_length=30, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
