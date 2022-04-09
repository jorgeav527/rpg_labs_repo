from django.contrib import admin

from paids.models import PaidItemQuatotion, PaidItemExecution, PaidItemLiquidation

# Register your models here.
@admin.register(PaidItemQuatotion)
class PaidItemQuatotionAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(PaidItemExecution)
class PaidItemExecutionAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(PaidItemLiquidation)
class PaidItemLiquidationAdmin(admin.ModelAdmin):
    pass
