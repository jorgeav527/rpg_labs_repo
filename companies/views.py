from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .forms import CompanyForm
from .models import Company


def company_list(request):
    companies_list = Company.objects.all()
    template_name = 'companies/company_list.html'
    title = 'registro de compañias'
    section = 'cotización'
    title_page = 'RE-COM'
    context = {
        'companies_list': companies_list,
        'title': title,
        'section': section,
        'title_page': title_page,
    }
    return render(request, template_name, context)


def company_list_create_update(request, id=None):
    companies_list = Company.objects.all()
    title = 'registro de compañias'
    section = 'cotización'
    title_page = 'RE-COM'
    obj = None
    context = {}
    # update view
    if id:
        obj = get_object_or_404(Company, id=id)
        form = CompanyForm(request.POST or None, instance=obj)
        context['form'] = form
        context['obj'] = obj
        if request.method == 'POST':
            form = CompanyForm(request.POST or None, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'Actualizado.')
                return redirect('companies:company_list_update', id=id)
            else:
                messages.error(request, 'Hubo un error en el Registro.')
    # create view
    elif id == None:
        form = CompanyForm()
        context['form'] = form
        if request.method == 'POST':
            form = CompanyForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, 'Creado.')
                return redirect('companies:company_list_create')
            else:
                messages.error(request, 'Hubo un error en el Registro.')

    context = {
        'companies_list': companies_list,
        'form': form,
        'obj': obj,
        'title': title,
        'title_page': title_page,
        'section': section
    }

    return render(request, 'companies/company_form_create_update.html', context)


def company_detail(request, id):
    template_name = 'companies/company_detail.html'
    companies_list = Company.objects.all()
    obj = get_object_or_404(Company, id=id)
    title = 'detalle compañia'
    title_page = 'INFO-COM'

    context = {
        'obj': obj,
        'companies_list': companies_list,
    }

    return render(request, template_name, context)


def company_delete(request, id):
    template_name = 'companies/company_table.html'
    obj = Company.objects.get(id=id)
    obj.delete()

    context = {
        'obj': obj,
    }

    return render(request, template_name, context)
