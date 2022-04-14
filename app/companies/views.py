from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
import csv

from companies.forms import CompanyForm
from companies.models import Company
from projects.models import Project

USER = get_user_model()


def list_company(request):
    qs = Company.objects.all()
    paginator = Paginator(qs, 25)
    page_number = request.GET.get("page")
    list_companies = paginator.get_page(page_number)
    context = {
        "list_companies": list_companies,
    }
    return render(request, "companies/list.html", context)


def search_list_company(request):
    query = request.GET.get("query")
    try:
        list_companies = Company.objects.filter(
            Q(social_reason__icontains=query) | Q(ruc__icontains=query)
        )
    except:
        list_companies = Company.objects.none()
    context = {
        "list_companies": list_companies,
    }
    return render(request, "companies/list.html", context)


def create_company(request):
    first_section = "-"
    second_section = "-"
    title = "crear organización"
    if request.method == "POST":
        form = CompanyForm(request.POST)
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
        form = CompanyForm()
    context = {
        "form": form,
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
    }
    return render(request, "companies/form.html", context)


def update_company(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    first_section = "-"
    second_section = "-"
    title = "editar organización"
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
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
        form = CompanyForm(instance=company)
    context = {
        "form": form,
        "company": company,
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
    }
    return render(request, "companies/form.html", context)


def detail_company(request, company_pk):
    company = get_object_or_404(Company, id=company_pk)
    context = {
        "company": company,
    }
    return render(request, "companies/detail.html", context)


@require_POST
def delete_company(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    company.delete()
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


def csv_company(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=compañias.csv"

    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model
    companies = Company.objects.all()

    # Add column headings to the csv file
    writer.writerow(
        [
            "id",
            "razon social",
            "dirección",
            "RUC",
            "tipo de compañía",
            "created (aaaa-mm-dd hh-mm-ss)",
            "updated (aaaa-mm-dd hh-mm-ss)",
        ]
    )

    # Loop Thu and output
    for item in companies:
        writer.writerow(
            [
                item.id,
                item.social_reason,
                item.address,
                item.ruc,
                item.get_type_company_display(),
                item.created.strftime("%Y-%m-%d %H:%M:%S"),
                item.updated.strftime("%Y-%m-%d %H:%M:%S"),
            ]
        )

    return response
