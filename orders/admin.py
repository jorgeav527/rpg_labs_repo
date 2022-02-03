from django.contrib import admin

from orders.models import Order, OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 1


@ admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_request', 'discount', 'get_sub_total',
                    'get_total_not_igv', 'get_igv', 'get_total_igv', 'created', 'updated')
    inlines = (OrderItemsInline,)


@ admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'test_lab',
                    'quantity', 'price', 'get_partial_igv')
