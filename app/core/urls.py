from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("registro/", views.enrolling, name="enrolling"),
    path("requerimiento/", views.requirement, name="requirement"),
]
