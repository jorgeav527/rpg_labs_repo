from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template

from xhtml2pdf import pisa

from tests_labs.models import TestLab
from orders.models import OrderLiquidation
from orders.forms import OrderLiquidationForm, OrderItemLiquidationFormset
from paids.forms import PaidItemLquidationFormset

from orders.utils import link_callback


def edit_order_liquidation(request, order_liquidation_pk):
    title = "cotización"
    first_section = "registro de requerimientos"
    second_section = "ensayos de ejecución"
    sub_first_section = "datos principales"
    sub_second_section = "lista de ensayos en liquidación"
    sub_third_section = "control de pagos realizados a la fecha"
    items_name = "orderitemliquidation_set"

    order_liquidation = get_object_or_404(OrderLiquidation, pk=order_liquidation_pk)
    if request.method == "POST":
        form_liquidation = OrderLiquidationForm(
            request.POST or None, instance=order_liquidation
        )
        form_item_liquidation = OrderItemLiquidationFormset(
            request.POST or None, instance=order_liquidation
        )
        form_item_paid = PaidItemLquidationFormset(
            request.POST or None, instance=order_liquidation
        )
        # print("running:", formset.is_valid())
        if (
            form_liquidation.is_valid()
            and form_item_liquidation.is_valid()
            and form_item_paid.is_valid()
        ):
            form_liquidation.save()
            form_item_liquidation.save()
            form_item_paid.save()
            # print(formset.cleaned_data)
            return redirect("core:requirement")
    else:
        form_liquidation = OrderLiquidationForm(instance=order_liquidation)
        form_item_liquidation = OrderItemLiquidationFormset(instance=order_liquidation)
        form_item_paid = PaidItemLquidationFormset(instance=order_liquidation)

    context = {
        "order_liquidation": order_liquidation,
        "form_liquidation": form_liquidation,
        "form_item_liquidation": form_item_liquidation,
        "form_item_paid": form_item_paid,
        "title": title,
        "first_section": first_section,
        "second_section": second_section,
        "sub_first_section": sub_first_section,
        "sub_second_section": sub_second_section,
        "sub_third_section": sub_third_section,
        "items_name": items_name,
    }
    return render(request, "orders/form_liquidation.html", context)


def liquidation_testlab_unit_quantity_price(request):
    items_name = "orderitemliquidation_set"
    url = request.get_full_path()
    # print("running url:", url)
    # print(url.split("-"))
    item = url.split("-")[1]
    # print("running item:", item)
    # print("running list:", list(request.GET.values()))
    test_lab_pk = list(request.GET.values())[0]
    test_lab = TestLab.objects.get(pk=test_lab_pk)
    # print("running item0:", item[0])
    # print("running test_lab_pk:", test_lab_pk)
    # print("running test_lab:", test_lab)
    context = {
        "test_lab": test_lab,
        "item": item[0],
        "items_name": items_name,
    }
    return render(request, "orders/testlab_unit_quantity_price.html", context)


def pdf_liquidation_order(request, order_liquidation_pk):
    order_obj = OrderLiquidation.objects.get(pk=order_liquidation_pk)
    title_head = "hoja de liquidación Nº"
    title_header = "laboratorio de mecánica de suelos, concreto y mezclas asfálticas"
    code_header = "RPG-FO-GT-18"
    version_header = "01"

    template_path = "orders/pdf_liquidation.html"
    context = {
        "order_obj": order_obj,
        "title_head": title_head,
        "title_header": title_header,
        "code_header": code_header,
        "version_header": version_header,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response
