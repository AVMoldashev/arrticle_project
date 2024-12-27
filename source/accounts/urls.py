from django.urls import path
from accounts.views import login_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login', LoginView.as_view(template_name="login.html"), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout')
]
