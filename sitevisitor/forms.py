from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    """A form for creating new users, with additional fields for profile information."""

    # Additional fields for the registration form
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name'
        })
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name'
        })
    )
    email = forms.EmailField(
        max_length=254, 
        required=True, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
    )
    phone = forms.CharField(
        max_length=15, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone'
        })
    )
    profile_description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Profile description',
            'style': 'height: 100px;',
            'rows': 3,
        })
    )
    profile_image = forms.ImageField(
        required=False, 
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file',
            'accept': 'image/*'
        })
    )
    id_proof = forms.ImageField(
        required=False, 
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file',
            'accept': 'image/*'
        })
    )
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')], 
        widget=forms.RadioSelect
    )

    class Meta:
        """Metadata for the form, linking it to the User model and defining the fields to be included."""
        
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2'
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Username'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Confirm Password'
            }),
        }
