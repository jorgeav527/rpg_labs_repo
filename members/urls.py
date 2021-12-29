from django.urls import path
from django.contrib.auth.views import LoginView

from .views import signup_admin, logout_request, login_request


app_name = 'members'

urlpatterns = [
    path('signup/admin/', signup_admin, name='signup_admin'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]
