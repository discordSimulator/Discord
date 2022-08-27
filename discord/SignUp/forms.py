from django import forms
from .models import SignUp
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class SignUpForm(forms.ModelForm):
    username_regex = RegexValidator(regex='^[a-zA-Z0-9.\-_]+$',
                                    message='Please use a combination of 0-9 a-z - _ ')

    username = forms.CharField(
        max_length=20,
        min_length=4,
        label='Username: ',
        error_messages={
            'min_length': 'Username is too short',
            'max_length': 'Username is too long',
            'required': 'please enter a username',
            'unique': 'Username already taken'
        },
        widget=forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'Username'}),
        validators=[username_regex])

    email = forms.CharField(
        label='Email: ',
        error_messages={
            'max_length': 'Email is too long',
            'required': 'please enter your email',
            'unique': 'Email already used'
        },
        widget=forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'Email'}))

    password = forms.CharField(
        max_length=50,
        min_length=7,
        label='Password: ',
        error_messages={
            'min_length': 'Password is too short',
            'max_length': 'Password is too long',
            'required': 'Please enter a password',
        },
        widget=forms.PasswordInput(attrs={'class': 'field-input', 'placeholder': 'Password', 'name': 'password'}))

    confirm_password = forms.CharField(
        label='Confirm Password: ',
        error_messages={

        },
        widget=forms.PasswordInput(attrs={'class': 'field-input', 'placeholder': 'Password', 'name': 'confirm-password'}
                                   ))

    class Meta:
        model = SignUp
        fields = ['username',
                  'email',
                  'password']
