from django.urls import path
from .views import home, registration, sign_in, forgot_password, otp_generation, resetting_password, error_page

urlpatterns = [
    path('', home, name='home'),
    path('sign_up/', registration, name='registration'),
    path('sign_in/', sign_in, name='login'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('otp/', otp_generation, name='otp'),
    path('resetting_password/', resetting_password, name='resetting_password'),
    path('404/', error_page, name='error_page'),
]
