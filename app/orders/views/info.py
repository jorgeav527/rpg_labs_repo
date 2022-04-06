from django.shortcuts import render, redirect, get_object_or_404


from orders.models import OrderQuatotion
from orders.forms import OrderInfoForm


def edit_order_quatotion_info(request, order_quatotion_pk):
    first_section = "registro de requerimientos"
    second_section = "información relacionada con el muestreo"
    title = "cotización"

    order_quatotion = get_object_or_404(OrderQuatotion, pk=order_quatotion_pk)
    form = OrderInfoForm(request.POST or None, instance=order_quatotion.orderinfo)
    if request.method == "POST":
        # print("running:", form.errors.values(), formset_order_items.is_valid())
        if form.is_valid():
            form.save()
            return redirect("core:requirement")
    else:
        form = OrderInfoForm(instance=order_quatotion.orderinfo)

    context = {
        "order_quatotion": order_quatotion,
        "form": form,
        "first_section": first_section,
        "second_section": second_section,
        "title": title,
    }
    return render(request, "orders/form_info.html", context)
