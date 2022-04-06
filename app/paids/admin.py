from django.contrib import admin

from paids.models import PaidItemQuatotion

# Register your models here.
@admin.register(PaidItemQuatotion)
class PaidItemQuatotionAdmin(admin.ModelAdmin):
    pass
