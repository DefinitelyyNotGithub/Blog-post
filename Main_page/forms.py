from django import forms
from .models import ContactUsModel


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        exclude = ['user', 'date', 'seen']

        name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
            'class': "col-md-12 col-sm-12"
        }))
        email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': "col-md-12 col-sm-12"
        }))
        subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
            'class': "col-md-12 col-sm-12"
        }))
        body = forms.CharField(min_length=20, max_length=600, widget=forms.Textarea(attrs={
            'class': "col-md-12 col-sm-12"
        }))