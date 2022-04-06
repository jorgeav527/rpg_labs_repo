from django.contrib import admin

from orders.models import (
    OrderQuatotion,
    OrderExecution,
    OrderLiquidation,
    OrderInfo,
    OrderItemQuatotion,
    OrderItemExecution,
    OrderItemLiquidation,
)


@admin.register(OrderQuatotion)
class OrderQuatotionAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderExecution)
class OrderExecutionAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderLiquidation)
class OrderLiquidationAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItemQuatotion)
class OrderItemQuatotionAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItemExecution)
class OrderItemExecutionAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItemLiquidation)
class OrderItemLiquidationAdmin(admin.ModelAdmin):
    pass
