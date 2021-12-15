from django.db import models

from companies.models import Company


class Project(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
