from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import get_user_model

from companies.forms import CompanyForm
from companies.models import Company
from projects.models import Project

USER = get_user_model()


def list_company(request):
    list_companies = Company.objects.all()
    context = {
        'list_companies': list_companies,
    }
    return render(request, 'companies/table.html', context)


def update_create_company(request, company_id=None):
    company_obj = None
    title = 'registro de compañias'
    section = 'cotización'
    title_page = 're-com'
    context = {}
    # update view
    if company_id:
        company_obj = get_object_or_404(Company, id=company_id)
        form_company = CompanyForm(request.POST or None, instance=company_obj)
        context['form_company'] = form_company
        context['company_obj'] = company_obj
        if request.method == 'POST':
            form_company = CompanyForm(
                request.POST or None, instance=company_obj)
            if form_company.is_valid():
                form_company.save()
                messages.success(request, 'Actualizado.')
                return redirect('companies:update_company', company_id=company_id)
            else:
                messages.error(request, 'Hubo un error en el Registro.')
    # create view
    elif company_id == None:
        form_company = CompanyForm()
        context['form_company'] = form_company
        if request.method == 'POST':
            form_company = CompanyForm(request.POST or None)
            if form_company.is_valid():
                form_company.save()
                messages.success(request, 'Creado.')
                return redirect('companies:create_company')
            else:
                messages.error(request, 'Hubo un error en el Registro.')

    context = {
        'form_company': form_company,
        'company_obj': company_obj,
        'title': title,
        'title_page': title_page,
        'section': section
    }

    return render(request, 'companies/form_update_create.html', context)


def detail_company(request, company_id):
    company_obj = get_object_or_404(Company, id=company_id)
    title = 'información'

    context = {
        'company_obj': company_obj,
        'title': title
    }

    return render(request, 'companies/detail.html', context)


def delete_company(request, company_id):
    company_obj = Company.objects.get(id=company_id)
    company_obj.delete()
    list_companies = Company.objects.all()
    context = {
        'list_companies': list_companies,
    }

    return render(request, 'companies/table.html', context)
