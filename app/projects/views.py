from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from projects.models import Project
from projects.forms import ProjectForm
from companies.models import Company

from members.choices import Roles, Professions

USER = get_user_model()


def list_project(request):
    list_projects = Project.objects.all()
    context = {
        "list_projects": list_projects,
    }
    return render(request, "projects/table.html", context)


def create_project(request, company_pk):
    first_section = "-"
    second_section = "-"
    title = "crear proyecto"
    company = Company.objects.get(pk=company_pk)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.company = company
            form_instance.save()
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
        form = ProjectForm()
    context = {
        "form": form,
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
    }
    return render(request, "projects/form.html", context)


def update_project(request, project_pk):
    first_section = "-"
    second_section = "-"
    title = "editar proyecto"
    project = get_object_or_404(Project, id=project_pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
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
        form = ProjectForm(instance=project)
    context = {
        "form": form,
        "project": project,
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
    }
    return render(request, "projects/form.html", context)


@require_POST
def delete_project(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    project.delete()
    return HttpResponse(
        "",
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
