from django import forms
from django.contrib.auth import (
    authenticate,
)
from django.contrib.auth.models import User
from usuarios.models import StandardUser
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(required=True, help_text='Email Requerido')

    class Meta:
        model = User

        fields = [
            'username', 'email', 'password1', 'password2', 'first_name', 'last_name'
        ]

        def clean_email(self):
            email = self.cleaned_data.get('email')
            email_exist = User.objets.filter(email=email).exists()
            if email_exist:
                raise ValidationError('Email ya registrado.')
            return email
        
        def save(self, commit=True):
            user= super().save(commit=False)
            user.email = self.cleaned_data.get('email')
            user.is_staff = False
            user.is_superuser = False
            if commit:
                user.save()
            return user


class LoginForm(forms.Form):

    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
    

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'email': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-class'}),
        }