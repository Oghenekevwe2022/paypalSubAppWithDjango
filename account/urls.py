from django.urls import path

from . import views

from django.contrib.auth import views as auth_views # For password management

urlpatterns = [
    
    path('', views.home, name= ""),
    
    path('register', views.register, name="register"),
    
    path('my-login', views.my_login, name="my-login"),
    
    path('user-logout', views.user_logout, name="user-logout"),
    
    #  Password management
    
    # 1 - Allow us to enter our email in order to receive a password reset link
    
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="password-reset.html"), name="reset_password"),
    
    # 2 - Show a success message stating that an email was sent to reset our password
    
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password-reset-sent.html"), name="password_reset_done"),
    
    # 3 - Send a link to our email, so we can reset our password + we will be prompted to enter our new password
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-form.html"), name="password_reset_confirm"),
    
    # 4 - Show a success message stating that our password was changed
    
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"), name="password_reset_complete"),
    
    #Email verification
    
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name="email-verification"),
    
    path('email-verification-sent', views.email_verification_sent, name="email-verification-sent"),
    
    path('email-verification-success', views.email_verification_success, name="email-verification-success"),
    
    path('email-verification-failed', views.email_verification_failed, name="email-verification-failed"),
]
