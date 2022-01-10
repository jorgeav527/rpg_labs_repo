from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from members.forms import AdminSignUpForm
from members.choices import Roles


def signup_admin(request):
    form_admin_signup = AdminSignUpForm()

    if request.method == 'POST':
        form_admin_signup = AdminSignUpForm(request.POST or None)
        if form_admin_signup.is_valid():
            f_a_s = form_admin_signup.save(commit=False)
            f_a_s.role = Roles.ADMIN
            f_a_s.is_staff = True
            f_a_s.save()
            email = form_admin_signup.cleaned_data.get('email')
            password = form_admin_signup.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, 'Usuario registrado y logeado.')
            return redirect('core:home')
        else:
            messages.error(request, 'Algo ocurrio.')

    context = {
        'form_admin_signup': form_admin_signup,
        'title': 'registro administración',
        'title_page': 're-adm',
    }
    return render(request, 'members/signup_admin.html', context)
