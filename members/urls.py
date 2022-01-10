from django.urls import path
from django.contrib.auth.views import LoginView

from members.views import signup_admin, logout_request, login_request, client_list, signup_client, client_delete


app_name = 'members'

urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    # admin urls
    path('signup/admin/', signup_admin, name='signup_admin'),
    # clients urls
    path('client/list/', client_list, name='client_list'),
    path('client/list/create/<int:id_company>/',
         signup_client, name='signup_client_create'),
    path('client/list/update/<int:id_u>/',
         signup_client, name='signup_client_update'),
    path('client/list/delete/<int:id>/',
         client_delete, name='client_delete_hx'),
]
