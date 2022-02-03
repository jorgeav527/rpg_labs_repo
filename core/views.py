from django.shortcuts import render
from django.template.response import TemplateResponse
from datetime import date


def home(request):
    title_page = 'home'
    today = date.today()
    context = {
        'title_page': title_page,
        'today': today,
    }
    if today.weekday() == 0:
        context['special_message'] = 'Happy Monday'
    return render(request, 'core/index.html', context)


def blog_view(request):
    title_page = 'change this'
    context = {
        "title_page": title_page,
    }
    return render(request, 'core/blog.html', context)


def enrolling(request):
    title = 'registro de compañias, clientes y projectos'
    section = 'cotización'
    title_page = 'registro'
    context = {
        'title': title,
        'section': section,
        'title_page': title_page,
    }
    return render(request, 'core/enrolling.html', context)


def requirement(request):
    title = 'registro de requerimientos'
    section = 'cotización'
    title_page = 'requerimiento'
    context = {
        'title': title,
        'section': section,
        'title_page': title_page,
    }
    return render(request, 'core/requirement.html', context)
