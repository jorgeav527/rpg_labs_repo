from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from members.forms import AuthenticationForm


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
