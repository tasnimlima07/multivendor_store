
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class  LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username','class': 'w-full py-4 px-6 rounded-xl'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'w-full py-4 px-6 rounded-xl'})
    )

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    

   
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username','class': 'w-full py-4 px-6 rounded-xl'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'w-full py-4 px-6 rounded-xl',})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'w-full py-4 px-6 rounded-xl',})
    )
    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repeat your password', 'class': 'w-full py-4 px-6 rounded-xl',})
    )


        
