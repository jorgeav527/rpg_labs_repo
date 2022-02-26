from import_export import resources

from tests_labs.models import TestInclude, TestLab


class TestIncludeResource(resources.ModelResource):
    class Meta:
        model = TestInclude


class TestLabResource(resources.ModelResource):
    class Meta:
        model = TestLab
        exclude = ("created", "updated")
