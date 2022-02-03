import os
from decimal import Decimal, ROUND_UP
from datetime import datetime

from django.contrib import admin
from django.db import models
from django.forms import inlineformset_factory

from tests_labs.models import TestLab

IGV = Decimal(os.environ.get('IGV')).quantize(Decimal('0.01'))


class Order(models.Model):
    number_request = models.CharField(
        max_length=20, default='codigo')
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(
        verbose_name='created at', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated at', auto_now=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return '(%s): %s' % (self.pk, self.discount)

    # @admin.display(description='Parcial')
    def get_sub_total(self):
        qs = self.order_items.filter(
            order=self.pk).values_list('quantity', 'price') or 0
        s_t = 0 if isinstance(qs, int) else sum(
            map(lambda q: q[0] * q[1], qs))
        sub_total = Decimal(s_t).quantize(Decimal('0.01'))
        return Decimal(sub_total/IGV or 0).quantize(Decimal('0.01'))

    def get_total_not_igv(self):
        return Decimal(self.get_sub_total() - self.discount or 0).quantize(Decimal('0.01'))

    def get_igv(self):
        return Decimal(self.get_total_not_igv() * Decimal(0.18) or 0).quantize(Decimal('0.01'))

    def get_total_igv(self):
        return Decimal(self.get_total_not_igv() + self.get_igv() or 0).quantize(Decimal('0.01'))

    def save(self, *args, **kwargs):
        # Generate the number_request (e.g. 2022-2-1-16-33-22)
        date = datetime.today()
        self.number_request = '%s-%s-%s-%s-%s-%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second)
        super(Order, self).save(*args, **kwargs)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
                              verbose_name='order', related_name='order_items', null=True, blank=True)
    test_lab = models.ForeignKey(TestLab, on_delete=models.SET_NULL,
                                 verbose_name='test lab', related_name='test_lab_items', null=True, blank=True)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sampling_by = models.BooleanField(null=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '(%s): %s - %s' % (self.pk, self.order, self.test_lab)

    def get_partial_igv(self):
        return Decimal(self.price * self.quantity).quantize(Decimal('0.01'), rounding=ROUND_UP)
