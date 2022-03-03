from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin

from tests_labs.models import TestLab, CharacteristicTestLab, TestInclude
from tests_labs.resources import TestIncludeResource, TestLabResource

from decimal import Decimal


class TestIncludeInline(admin.TabularInline):
    model = TestInclude
    fk_name = "to_test"


@admin.register(TestLab)
class TestLabAdmin(ImportExportModelAdmin):
    resource_class = TestLabResource
    list_display = (
        "pk",
        "characteristic",
        "name_test",
        "basic_norm",
        "refer_norm",
        "unit",
        "quantity",
        "price",
        "is_parent",
        "get_partial_igv",
        "get_partial_not_igv",
    )
    list_display_links = ("name_test",)
    radio_fields = {"characteristic": admin.HORIZONTAL}
    search_fields = ["name_test"]
    inlines = [
        TestIncludeInline,
    ]

    # get the instance obj
    # def get_form(self, request, obj=None, **kwargs):
    #     self.instance = obj
    #     return super().get_form(request, obj=obj, **kwargs)

    # display all the tests labs but not the same
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'child_tests':
    #         kwargs['queryset'] = TestLab.objects.exclude(pk=self.instance.pk)
    #     return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # After save get the others test related by the include and update them
        if not obj.is_parent:
            q = TestInclude.objects.filter(from_test=obj.pk)
            print("running:q", q)
            q_list = list(q.values_list("to_test", flat=True))
            print("running:q_list", q_list)

            total_test_parent = Decimal(0)
            for i in TestLab.objects.filter(pk__in=q_list):
                i.price = total_test_parent
                print("running:i.price", i.price)
                total_test_child = Decimal(0)
                for _i in i.to_test.all():
                    to_test = TestLab.objects.get(pk=_i.from_test_id)
                    total_test_child += Decimal(to_test.get_partial_igv())
                i.price = total_test_child
                i.save()


@admin.register(CharacteristicTestLab)
class CharacteristicTestLabAdmin(admin.ModelAdmin):
    list_display = ("pk", "lab", "matrix")
    radio_fields = {"matrix": admin.VERTICAL, "lab": admin.HORIZONTAL}


@admin.register(TestInclude)
class TestIncludeAdmin(ImportExportModelAdmin):
    resource_class = TestIncludeResource
    list_display = ("pk", "to_test", "from_test")
