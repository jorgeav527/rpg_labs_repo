from django.urls import path
from django.contrib.auth.views import LoginView

from members import views


app_name = "members"

urlpatterns = [
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    # admin urls
    path("signup/admin/", views.signup_admin, name="signup_admin"),
    # clients urls
    path("list/", views.list_client, name="list_client"),
    path("create/<int:company_pk>/", views.create_client, name="create_client"),
    path("update/<int:user_pk>/", views.update_client, name="update_client"),
    path("delete/<int:user_pk>/", views.delete_client, name="delete_client"),
]
