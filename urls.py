from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
urlpatterns = [
    path('signup',views.signup, name='signup-page'),
    path('main',views.done, name='logged-page'),
    path('',views.login_page, name='login-page'),
    path('logout',views.logout_page, name='logout-page'),

    path('reset_password/',
         auth_view.PasswordResetView.as_view(template_name='reset_password.html'),
         name="reset_password"),

    path('reset_password_sent/',
         auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name="password_reset_complete"),
]
