from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model

from members.forms import ClientSignUpForm
from members.models import ClientProfile
from members.choices import Roles, Professions
from companies.models import Company

USER = get_user_model()
RAW_PASSWORD = 'rpgclient123'


def client_list(request):
    client_list = USER.clientprofile.get_queryset()
    template_name = 'members/client/client_list.html'
    title = 'registro de clientes'
    section = 'cotización'
    title_page = 're-cli'
    context = {
        'client_list': client_list,
        'title': title,
        'section': section,
        'title_page': title_page,
    }
    return render(request, template_name, context)


def signup_client(request, id_company=None, id_u=None):
    obj_c_p = None
    obj_company = None
    title = 'registro de clientes'
    section = 'cotización'
    title_page = 're-cli'
    context = {}
    # update view
    if id_u and id_company == None:
        obj_c_p = get_object_or_404(USER, id=id_u)
        form_client_signup = ClientSignUpForm(
            request.POST or None, instance=obj_c_p)
        context['form_client_signup'] = form_client_signup
        context['obj_c_p'] = obj_c_p
        if request.method == 'POST':
            form_client_signup = ClientSignUpForm(
                request.POST or None, instance=obj_c_p)
            if form_client_signup.is_valid():
                form_client_signup.save()
                messages.success(
                    request, f'Usuario registrado como cliente fue actualizado.')
                return redirect('members:signup_client_update', id_u=id_u)
            else:
                messages.error(request, 'Algo ocurrio.')
    # create view
    if id_company and id_u == None:
        form_client_signup = ClientSignUpForm()
        obj_company = Company.objects.get(id=id_company)
        context['obj_company'] = obj_company
        context['form_client_signup'] = form_client_signup
        if request.method == 'POST':
            form_client_signup = ClientSignUpForm(request.POST or None)
            if form_client_signup.is_valid():
                f_c_s = form_client_signup.save(commit=False)
                f_c_s.role = Roles.CLIENT
                f_c_s.set_password(RAW_PASSWORD)
                f_c_s.save()
                ClientProfile.objects.filter(
                    id=f_c_s.clientprofile.id).update(company=obj_company)
                messages.success(request, f'Usuario registrado como cliente.')
                return redirect('members:signup_client_create', id_company=id_company)
            else:
                messages.error(request, 'Algo ocurrio.')

    context = {
        'obj_c_p': obj_c_p,
        'obj_company': obj_company,
        'form_client_signup': form_client_signup,
        'title': 'registro cliente',
        'title_page': 're-cli',
    }
    return render(request, 'members/client/client_form_create_update.html', context)


def client_delete(request, id):
    template_name = 'companies/company_detail.html'
    obj = get_object_or_404(USER, id=id)
    obj_client = obj.clientprofile.company_id
    obj.delete()

    context = {
        'obj': obj,
    }

    return redirect('companies:company_detail_hx', id=obj_client)
