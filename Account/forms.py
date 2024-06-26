from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .admin import User as User2
from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User2
        fields = ["email", ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User2
        fields = ["email", "password", "is_active", "is_admin"]


class LogInForm(forms.Form):
    username = forms.CharField(required=None, widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': "Email"
    }))
    password = forms.CharField(required=None, widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': "password"
    }))


class RegisterForm(forms.Form):
    username = forms.CharField(required=None, widget=forms.EmailInput(attrs={
        'placeholder': "Email",
        'class': "form-control"
    }))
    password = forms.CharField(required=None, max_length=16, min_length=4, widget=forms.PasswordInput(attrs={
        'placeholder': "password",
        'class': "form-control"
    }))
    password_confirm = forms.CharField(required=None, widget=forms.PasswordInput(attrs={
        'placeholder': "confirm password",
        'class': "form-control"
    }))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(email__iexact=username).exists():
            raise ValidationError("this user already exists !")
        return username

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise ValidationError("Not the same password")

