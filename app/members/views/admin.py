from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from members.forms import AdminSignUpForm
from members.choices import Roles


def signup_admin(request):
    first_section = "re-adm"
    title = "registro administración"

    if request.method == "POST":
        form = AdminSignUpForm(request.POST or None)
        if form.is_valid():
            f_a_s = form.save(commit=False)
            f_a_s.role = Roles.ADMIN
            f_a_s.is_staff = True
            f_a_s.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "Usuario registrado y logeado.")
            return redirect("core:home")
    else:
        form = AdminSignUpForm()

    context = {
        "form": form,
        "title": title,
        "first_section": first_section,
    }
    return render(request, "members/admin/form.html", context)
