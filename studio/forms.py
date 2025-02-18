from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class ContactForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Your Message", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']