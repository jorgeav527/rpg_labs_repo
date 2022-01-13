from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model

from projects.models import Project
from projects.forms import ProjectForm
from companies.models import Company

from members.choices import Roles, Professions

USER = get_user_model()


def list_project(request):
    list_projects = Project.objects.all()
    context = {
        'list_projects': list_projects,
    }
    return render(request, 'projects/table.html', context)


def update_create_list_project(request, company_id=None, project_id=None):
    project_obj = None
    company_obj = None
    title = 'registro de projectos'
    section = 'cotización'
    title_page = 're-pro'
    context = {}
    # update view
    if project_id and company_id == None:
        project_obj = get_object_or_404(Project, id=project_id)
        form_project = ProjectForm(
            request.POST or None, instance=project_obj)
        context['form_project'] = form_project
        context['project_obj'] = project_obj
        if request.method == 'POST':
            form_project = ProjectForm(
                request.POST or None, instance=project_obj)
            if form_project.is_valid():
                form_project.save()
                messages.success(
                    request, f'El proyecto fue actualizado.')
                return redirect('projects:update_project', project_id=project_id)
            else:
                messages.error(request, 'Algo ocurrio.')
    # create view
    if company_id and project_id == None:
        form_project = ProjectForm()
        company_obj = Company.objects.get(id=company_id)
        context['company_obj'] = company_obj
        context['form_project'] = form_project
        if request.method == 'POST':
            form_project = ProjectForm(request.POST or None)
            if form_project.is_valid():
                p_f = form_project.save(commit=False)
                p_f.company = company_obj
                p_f.save()
                messages.success(request, f'El projecto fue registrado.')
                return redirect('projects:create_project', company_id=company_id)
            else:
                messages.error(request, 'Algo ocurrio.')

    context = {
        'project_obj': project_obj,
        'company_obj': company_obj,
        'form_project': form_project,
        'title': title,
        'section': section,
        'title_page': title_page,
    }
    return render(request, 'projects/form_create_update.html', context)


def delete_project(request, project_id):
    project_obj = get_object_or_404(Project, id=project_id)
    project_obj_company_id = project_obj.company_id
    project_obj.delete()

    return redirect('companies:detail_company_hx', company_id=project_obj_company_id)
