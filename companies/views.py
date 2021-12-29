from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .forms import CompanyForm
from .models import Company


def company_create_update(request, id=None):
    companies_list = Company.objects.all()
    title = 'Registro de Compañias'
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
                return redirect('companies:company_create')
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
                return redirect('companies:company_create')
            else:
                messages.error(request, 'Hubo un error en el Registro.')

    context = {
        'companies_list': companies_list,
        'form': form,
        'obj': obj,
        'title': title,
        'title_page': title_page,
    }

    return render(request, 'companies/company_create_update.html', context)


def company_detail(request, id):
    obj = Company.objects.get(id=id)
    title = 'detalle compañia'

    context = {
        'obj': obj,
        'title': title
    }

    return render(request, 'companies/company_detail.html', context)


def company_delete(request, id):
    obj = Company.objects.get(id=id)
    title = 'eliminar compañia'
    obj.delete()

    context = {
        'obj': obj,
        'title': title
    }

    return render(request, 'companies/company_table.html', context)
