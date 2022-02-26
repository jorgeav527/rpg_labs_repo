from django.shortcuts import render
from django.template.response import TemplateResponse
from datetime import date

from core import utils


def index(request):
    title_head = "index"
    title = "index"
    section = "index"
    context = {
        "title": title,
        "section": section,
        "title_head": title_head,
    }
    return render(request, "core/index.html", context)


def home(request):
    title_head = "home"
    title = "home"
    section = "bienvenido"
    today = utils.generate_time_str_num()
    context = {
        "title": title,
        "section": section,
        "title_head": title_head,
        "today": today,
    }
    return render(request, "core/home.html", context)


def blog(request):
    title_head = "blog"
    title = "blog"
    section = "blog"
    context = {
        "title": title,
        "section": section,
        "title_head": title_head,
    }
    return render(request, "core/blog.html", context)


def enrolling(request):
    title = "cotización"
    section = "registro de compañias, clientes y proyectos"
    title_head = "registro"
    context = {
        "title": title,
        "section": section,
        "title_head": title_head,
    }
    return render(request, "core/enrolling.html", context)


def requirement(request):
    title = "cotización"
    section = "registro de requerimientos"
    title_head = "requerimiento"
    context = {
        "title": title,
        "section": section,
        "title_head": title_head,
    }
    return render(request, "core/requirement.html", context)
