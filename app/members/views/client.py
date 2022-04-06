from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.http import require_POST


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


def create_client(request, company_pk):
    first_section = "-"
    second_section = "-"
    title = "crear cliente/funcionario"
    company = Company.objects.get(pk=company_pk)
    if request.method == "POST":
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.role = Roles.CLIENT
            form_instance.set_password(RAW_PASSWORD)
            form_instance.save()
            ClientProfile.objects.filter(pk=form_instance.clientprofile.pk).update(
                company=company
            )
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "companyListChanged"}
                # headers={
                #     "HX-Trigger": json.dumps(
                #         {
                #             "movieListChanged": None,
                #             "showMessage": f"{company.title} added.",
                #         }
                #     )
                # },
            )
    else:
        form = ClientSignUpForm()
    context = {
        "form": form,
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
    }
    return render(request, "members/client/form.html", context)


def update_client(request, user_pk):
    first_section = "-"
    second_section = "-"
    title = "editar cliente/funcionario"
    client_user = get_object_or_404(USER, pk=user_pk)
    if request.method == "POST":
        form = ClientSignUpForm(request.POST, instance=client_user)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={"HX-Trigger": "companyListChanged"}
                # headers={
                #     "HX-Trigger": json.dumps(
                #         {
                #             "movieListChanged": None,
                #             "showMessage": f"{company.title} added.",
                #         }
                #     )
                # },
            )
    else:
        form = ClientSignUpForm(instance=client_user)
    context = {
        "form": form,
        "client_user": client_user,
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
    }
    return render(request, "members/client/form.html", context)


@require_POST
def delete_client(request, user_pk):
    user = get_object_or_404(USER, pk=user_pk)
    user.delete()
    return HttpResponse(
        status=204,
        headers={"HX-Trigger": "companyListChanged"}
        # headers={
        #     "HX-Trigger": json.dumps(
        #         {
        #             "movieListChanged": None,
        #             "showMessage": f"{company.title} added.",
        #         }
        #     )
        # },
    )
