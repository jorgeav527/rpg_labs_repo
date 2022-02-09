from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from tests_labs.models import TestLab

from orders.models import Order, OrderItems
from projects.models import Project
from members.models import ClientProfile
from orders.forms import OrderForm, OrderItemsForm, OrderItemsFormset


def list_order(request):
    list_orders = Order.objects.all()
    context = {
        'list_orders': list_orders,
    }
    return render(request, 'orders/table.html', context)


def create_order(request):
    title = 'registro de requerimientos'
    section = 'cotización'
    title_page = 'requerimiento'
    order_instance = Order()
    form_order = OrderForm(request.POST or None,
                           instance=order_instance, prefix='main')
    formset_order_items = OrderItemsFormset(
        request.POST or None, instance=order_instance, prefix='items')
    if request.method == 'POST':
        # print('running:', form_order.errors.values(),
        #       formset_order_items.is_valid())
        if form_order.is_valid() and formset_order_items.is_valid():
            form_order.save()
            formset_order_items.save()
            return redirect('core:requirement')
        else:
            messages.error(request, 'Hubo un error en el Registro.')
    context = {
        'form_order': form_order,
        'formset_order_items': formset_order_items,
        'title': title,
        'section': section,
        'title_page': title_page,
    }
    return render(request, 'orders/form_create_update.html', context)


def update_order(request, order_id):
    title = 'registro de requerimientos'
    section = 'cotización'
    title_page = 'requerimiento'
    order_instance = get_object_or_404(Order, id=order_id)
    form_order = OrderForm(request.POST or None,
                           instance=order_instance, prefix='main')
    formset_order_items = OrderItemsFormset(
        request.POST or None, instance=order_instance, prefix='items')
    if request.method == 'POST':
        if form_order.is_valid() and formset_order_items.is_valid():
            form_order.save()
            formset_order_items.save()
            return redirect('core:requirement')
        else:
            messages.error(request, 'Hubo un error en el Registro.')
    context = {
        'order_instance': order_instance,
        'form_order': form_order,
        'formset_order_items': formset_order_items,
        'title': title,
        'section': section,
        'title_page': title_page,
    }
    return render(request, 'orders/form_create_update.html', context)


def delete_order(request, order_id):
    order_obj = Order.objects.get(id=order_id)
    order_obj.delete()
    return HttpResponse('')


def create_order_item_row(request):
    order_item_form = OrderItemsForm()
    context = {'order_item_form': order_item_form}
    return render(request, 'orders/order_item_row.html', context)


def test_lab_price(request):
    url = request.get_full_path()
    # print('running url', url)
    # print(url.split('-'))
    item = url.split('-')[1]
    # print('running item', item)
    # print('list', list(request.GET.values()))
    test_lab_pk = list(request.GET.values())[0]
    test_lab = TestLab.objects.get(pk=test_lab_pk)
    # print('running item0', item[0])
    # print('running test_lab_pk', test_lab_pk)
    # print('running test_lab', test_lab)
    context = {
        'test_lab': test_lab,
        'item': item[0]
    }
    return render(request, 'orders/test_lab_price.html', context)


def characteristic_test_lab(request):
    url = request.get_full_path()
    # print('running url', url)
    # print('running url split', url.split('-'))
    item = url.split('-')[1]
    # print('running item', item, item[0])
    # print('running list', list(request.GET.values()))
    characteristictestlab_pk = list(request.GET.values())[0]
    test_lab_qs = TestLab.objects.filter(
        characteristic=characteristictestlab_pk)
    # print('running characteristictestlab_pk', characteristictestlab_pk)
    # print('running test_lab_qs', test_lab_qs)
    context = {
        'test_lab_qs': test_lab_qs,
        'item': item[0]
    }
    return render(request, 'orders/characteristictestlab_test_lab.html', context)


def delete_order_item_row(request, order_item_id):
    order_item = OrderItems.objects.get(pk=order_item_id)
    order_item.delete()
    return HttpResponse('')


def company_project_client(request):
    company_pk = list(request.GET.values())[0]
    project_qs = Project.objects.filter(
        company=company_pk)
    clientprofile_qs = ClientProfile.objects.filter(
        company=company_pk)
    # print('running company_pk', company_pk)
    # print('running project_qs', project_qs)
    # print('running clientprofile_qs', clientprofile_qs)
    context = {
        'project_qs': project_qs,
        'clientprofile_qs': clientprofile_qs,
    }
    return render(request, 'orders/company_project_client.html', context)
