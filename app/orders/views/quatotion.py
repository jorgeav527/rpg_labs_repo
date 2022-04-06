from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.views.decorators.http import require_POST
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from xhtml2pdf import pisa

from tests_labs.models import TestLab
from orders.models import OrderQuatotion
from orders.forms import OrderQuatotionForm, OrderItemQuatotionFormset
from paids.forms import PaidItemQuatotionFormset

from orders.utils import link_callback


def list_order_quatotion(request):
    qs = OrderQuatotion.objects.all()
    paginator = Paginator(qs, 40)
    page_number = request.GET.get("page")
    list_orders = paginator.get_page(page_number)
    context = {
        "list_orders": list_orders,
    }
    return render(request, "orders/list.html", context)


def search_list_order_quatotion(request):
    query = request.GET.get("query")
    try:
        list_orders = OrderQuatotion.objects.filter(pk=query)
    except:
        list_orders = OrderQuatotion.objects.none()
    context = {
        "list_orders": list_orders,
    }
    return render(request, "orders/list.html", context)


def create_order_quatotion(request):
    title = "cotización"
    first_section = "registro de requerimientos"
    second_section = "ensayos de cotización"
    sub_first_section = "datos principales"
    sub_second_section = "lista de ensayos cotizados"
    sub_third_section = "condiciones de pago"
    items_name = "orderitemquatotion_set"

    order_quatotion = OrderQuatotion()
    if request.method == "POST":
        form_quatotion = OrderQuatotionForm(
            request.POST or None, instance=order_quatotion
        )
        form_item_quatotion = OrderItemQuatotionFormset(
            request.POST or None, instance=order_quatotion
        )
        form_item_paid = PaidItemQuatotionFormset(
            request.POST or None, instance=order_quatotion
        )
        if (
            form_quatotion.is_valid()
            and form_item_quatotion.is_valid()
            and form_item_paid.is_valid()
        ):
            form_quatotion.save()
            form_item_quatotion.save()
            form_item_paid.save()
            return redirect("core:requirement")
    else:
        form_quatotion = OrderQuatotionForm(instance=order_quatotion)
        form_item_quatotion = OrderItemQuatotionFormset(instance=order_quatotion)
        form_item_paid = PaidItemQuatotionFormset(instance=order_quatotion)

    context = {
        "order_quatotion": order_quatotion,
        "form_quatotion": form_quatotion,
        "form_item_quatotion": form_item_quatotion,
        "form_item_paid": form_item_paid,
        "title": title,
        "first_section": first_section,
        "second_section": second_section,
        "sub_first_section": sub_first_section,
        "sub_second_section": sub_second_section,
        "sub_third_section": sub_third_section,
        "items_name": items_name,
    }
    return render(request, "orders/form_quatotion.html", context)


def update_order_quatotion(request, order_quatotion_pk):
    title = "cotización"
    first_section = "registro de requerimientos"
    second_section = "ensayos de cotización"
    sub_first_section = "datos principales"
    sub_second_section = "lista de ensayos cotizados"
    sub_third_section = "condiciones de pago"
    items_name = "orderitemquatotion_set"

    order_quatotion = get_object_or_404(OrderQuatotion, pk=order_quatotion_pk)
    if request.method == "POST":
        form_quatotion = OrderQuatotionForm(
            request.POST or None, instance=order_quatotion
        )
        form_item_quatotion = OrderItemQuatotionFormset(
            request.POST or None, instance=order_quatotion
        )
        form_item_paid = PaidItemQuatotionFormset(
            request.POST or None, instance=order_quatotion
        )
        # print("running:", formset.is_valid())
        if (
            form_quatotion.is_valid()
            and form_item_quatotion.is_valid()
            and form_item_paid.is_valid()
        ):
            form_quatotion.save()
            form_item_quatotion.save()
            form_item_paid.save()
            # print(formset.cleaned_data)
            return redirect("core:requirement")
    else:
        form_quatotion = OrderQuatotionForm(instance=order_quatotion)
        form_item_quatotion = OrderItemQuatotionFormset(instance=order_quatotion)
        form_item_paid = PaidItemQuatotionFormset(instance=order_quatotion)

    context = {
        "order_quatotion": order_quatotion,
        "form_quatotion": form_quatotion,
        "form_item_quatotion": form_item_quatotion,
        "form_item_paid": form_item_paid,
        "title": title,
        "first_section": first_section,
        "second_section": second_section,
        "sub_first_section": sub_first_section,
        "sub_second_section": sub_second_section,
        "sub_third_section": sub_third_section,
        "items_name": items_name,
    }
    return render(request, "orders/form_quatotion.html", context)


@require_POST
def delete_order_quatotion(request, order_quatotion_pk):
    order_quatotion = OrderQuatotion.objects.get(pk=order_quatotion_pk)
    order_quatotion.delete()
    return HttpResponse(
        status=204,
        headers={"HX-Trigger": "orderListChanged"}
        # headers={
        #     "HX-Trigger": json.dumps(
        #         {
        #             "movieListChanged": None,
        #             "showMessage": f"{company.title} added.",
        #         }
        #     )
        # },
    )


def quatotion_testlab_unit_quantity_price(request):
    items_name = "orderitemquatotion_set"
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


def pdf_quatotion_order(request, order_quatotion_pk):
    order_obj = OrderQuatotion.objects.get(pk=order_quatotion_pk)
    title_head = "cotización Nº"
    title_header = "laboratorio de mecánica de suelos, concreto y mezclas asfálticas"
    code_header = "RPG-FO-GT-11"
    version_header = "01"

    template_path = "orders/pdf_quatotion.html"
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


def pdf_requirement_order(request, order_quatotion_pk):
    order_obj = OrderQuatotion.objects.get(pk=order_quatotion_pk)
    title_head = f"requerimiento Nº"
    title_header = "determinación y revisión de requisitos de los servicios de ensayo, estudios geotécnicos y estudios de mecánica de suelos"
    code_header = "RPG-FO-GT-10"
    version_header = "01"

    template_path = "orders/pdf_requirement.html"
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
