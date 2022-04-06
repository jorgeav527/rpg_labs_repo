from django.shortcuts import render

from core import utils


def home(request):
    first_section = "nosotros"
    second_section = "home"
    title = "bienvenido"
    today = utils.generate_time_str_num()
    context = {
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
        "today": today,
    }
    return render(request, "core/home.html", context)


def enrolling(request):
    first_section = "cotización"
    second_section = "registro de compañias, clientes y proyectos"
    title = "registro"
    context = {
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
    }
    return render(request, "core/enrolling.html", context)


def requirement(request):
    first_section = "cotización"
    second_section = "registro de requerimientos"
    title = "requerimiento"
    context = {
        "second_section": second_section,
        "first_section": first_section,
        "title": title,
    }
    return render(request, "core/requirement.html", context)
