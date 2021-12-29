from django.db import models


class Company(models.Model):
    social_reason = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    ruc = models.PositiveBigIntegerField(unique=True)
    created = models.DateTimeField("created at", auto_now_add=True)
    updated = models.DateTimeField("updated at", auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return f'{self.social_reason} {self.ruc}'
