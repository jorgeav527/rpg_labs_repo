from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model

from members.forms import ClientSignUpForm
from members.models import ClientProfile
from members.choices import Roles, Professions
from companies.models import Company

USER = get_user_model()
RAW_PASSWORD = "rpgclient123"


def list_client(request):
    list_clients = USER.clientprofile.get_queryset()
    context = {
        "list_clients": list_clients,
    }
    return render(request, "members/client/table.html", context)


def update_create_signup_client(request, company_id=None, user_id=None):
    user_obj = None
    company_obj = None
    title = "cotización"
    section = "registro de clientes"
    title_head = "re-cli"
    context = {}
    # update view
    if user_id and company_id == None:
        user_obj = get_object_or_404(USER, id=user_id)
        form_client_signup = ClientSignUpForm(request.POST or None, instance=user_obj)
        context["form_client_signup"] = form_client_signup
        context["user_obj"] = user_obj
        if request.method == "POST":
            form_client_signup = ClientSignUpForm(
                request.POST or None, instance=user_obj
            )
            if form_client_signup.is_valid():
                form_client_signup.save()
                messages.success(
                    request, f"Usuario registrado como cliente fue actualizado."
                )
                return redirect("members:update_signup_client", user_id=user_id)
            else:
                messages.error(request, "Algo ocurrio.")
    # create view
    if company_id and user_id == None:
        form_client_signup = ClientSignUpForm()
        company_obj = Company.objects.get(id=company_id)
        context["company_obj"] = company_obj
        context["form_client_signup"] = form_client_signup
        if request.method == "POST":
            form_client_signup = ClientSignUpForm(request.POST or None)
            if form_client_signup.is_valid():
                f_c_s = form_client_signup.save(commit=False)
                f_c_s.role = Roles.CLIENT
                f_c_s.set_password(RAW_PASSWORD)
                f_c_s.save()
                ClientProfile.objects.filter(id=f_c_s.clientprofile.id).update(
                    company=company_obj
                )
                messages.success(request, f"Usuario registrado como cliente.")
                return redirect("members:create_signup_client", company_id=company_id)
            else:
                messages.error(request, "Algo ocurrio.")

    context = {
        "user_obj": user_obj,
        "company_obj": company_obj,
        "form_client_signup": form_client_signup,
        "title": title,
        "section": section,
        "title_head": title_head,
    }
    return render(request, "members/client/form_update_create.html", context)


def client_delete(request, user_id):
    user_obj = get_object_or_404(USER, id=user_id)
    user_clientprofile_company_id = user_obj.clientprofile.company_id
    user_obj.delete()

    return redirect(
        "companies:detail_company_hx", company_id=user_clientprofile_company_id
    )
