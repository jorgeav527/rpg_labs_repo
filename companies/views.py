from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .forms import CompanyForm
from .models import Company


def company_list(request):
    companies_list = Company.objects.all()
    form = CompanyForm()
    title = "Registro de Compañias"

    context = {
        'companies_list': companies_list,
        'title': title,
        'form': form
    }
    return render(request, 'companies/company_list.html', context=context)


def company_create(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Creado")
        return redirect('companies:company_list')

    context = {
        'form': form
    }

    return render(request, 'companies/company_form.html', context=context)


# def company_list(request):
#     form = CompanyForm(request.POST or None)
#     companies = Company.objects.all()
#     title = "Lista de Compañias"

#     context = {
#         'object_list': companies,
#         'form': form,
#         'title': title,
#     }
#     return render(request, 'companies/company_list.html', context)
