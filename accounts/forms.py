from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='UserName',
                               max_length=100,
                               min_length=3,
                               widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField()
    password1 = forms.CharField(label='Password',
                                max_length=20,
                                min_length=5,
                                widget=forms.PasswordInput)

    password2 = forms.CharField(label='Confirm password',
                                max_length=20,
                                min_length=5,
                                widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError("Please Choose a Different Username")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError("Email already exists, please choose a different one")
        return email

    def clean_password2(self):
        #cleaned_data = super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError("Both passwords should match")


