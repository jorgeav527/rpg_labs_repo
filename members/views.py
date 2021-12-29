from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import AdminSignUpForm, AuthenticationForm


def signup_admin(request):
    form = AdminSignUpForm()

    if request.method == 'POST':
        form = AdminSignUpForm(request.POST or None)
        if form.is_valid():
            u = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, 'Usuario registrado y logeado.')
            return redirect('core:home')
        else:
            messages.error(request, 'Algo ocurrio.')

    context = {
        'form': form,
        'title': 'registro administración',
        'title_page': 're-adm',
    }
    return render(request, 'members/signup_admin.html', context)


def login_request(request):
    msg = None
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(
                        request, 'Usuario correctamente y logeado.')
                    return redirect('core:home')
        else:
            messages.error(request, 'Algo ocurrio.')

    context = {
        'form': form,
        'title': 'ingreso',
        'title_page': 'login',
    }

    return render(request, 'members/login.html', context)


def logout_request(request):
    logout(request)
    messages.success(request, 'Se cerro la sesión correctamente!')
    return redirect('members:login')
