from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import User_Table, Blog, Comment

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}), max_length=15, required=True)
    profile_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)
    id_proof = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)
    profile_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tell us about yourself...'}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone', 'profile_image', 'id_proof', 'profile_description']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254, 
        required=True, 
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="Password", 
        required=True, 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'blog_image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your blog title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your blog content here.'}),
            'blog_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'status': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'})
        }


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )
    username = forms.CharField(
        max_length=150,  # Ensure it matches your User model max_length
        required=True, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    email = forms.EmailField(
        max_length=254, 
        required=True, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )

    class Meta:
        model = User_Table
        fields = ['phone', 'profile_image', 'cover_photo', 'id_proof', 'profile_description']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'cover_photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'id_proof': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'profile_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tell us about yourself...'})
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your old password'
        })
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your new password'
        })
    )
    new_password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your new password'
        })
    )

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']
