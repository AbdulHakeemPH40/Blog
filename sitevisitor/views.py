from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from userpanel.models import Blog, User_Table
from .forms import RegistrationForm
from userpanel.forms import LoginForm


def home(request):
    """Render the home page with a list of published blogs."""
    published_blogs = Blog.objects.filter(status='published').order_by('-created_at')
    context = {'blogs': published_blogs}
    return render(request, 'sitevisitor/home.html', context)


def registration(request):
    """Handle the user registration process."""
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST, request.FILES)
        
        if registration_form.is_valid():
            new_user = registration_form.save()

            # Create a corresponding user profile
            User_Table.objects.create(
                user=new_user,
                phone=registration_form.cleaned_data['phone'],
                profile_image=registration_form.cleaned_data['profile_image'],
                id_proof=registration_form.cleaned_data['id_proof'],
                profile_description=registration_form.cleaned_data['profile_description']
            )
            auth_login(request, new_user)
            messages.success(request, "Registration successful.")
            return redirect('user_home')
        else:
            messages.error(request, "Registration unsuccessful. Please correct the errors below.")
    else:
        registration_form = RegistrationForm()

    context = {'form': registration_form}
    return render(request, 'sitevisitor/registration.html', context)


def forgot_password(request):
    """Render the 'Forgot Password' page."""
    return render(request, 'sitevisitor/forgot_password.html')


def otp_generation(request):
    """Render the OTP generation page."""
    return render(request, 'sitevisitor/otp.html')


def resetting_password(request):
    """Render the password reset page."""
    return render(request, 'sitevisitor/reset_password.html')


def error_page(request):
    """Render the custom 404 error page."""
    return render(request, 'sitevisitor/404.html')

def sign_in(request):
    """Handle the sign-in process for site visitors."""
    if request.method == 'POST':
        login_form = LoginForm(request, data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_staff:  # Redirect staff users to the admin panel
                    messages.success(request, "Access Denied: Staff users are not permitted to access the User Panel.!")
                    return redirect('login')

                user_profile = User_Table.objects.get(user=user)
                
                if user_profile.is_blocked:
                    messages.error(request, "Your account is blocked. Please contact the administrator.")
                    return redirect('sign_in')
                
                auth_login(request, user)
                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect('user_home')

            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    else:
        login_form = LoginForm()

    context = {'form': login_form}
    return render(request, 'sitevisitor/login.html', context)
