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
