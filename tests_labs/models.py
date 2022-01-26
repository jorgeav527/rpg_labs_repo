from django.db import models

from tests_labs.choices import Matrices, Labs, Unit


class CharacteristicTestLab(models.Model):
    lab = models.CharField(
        max_length=8, choices=Labs.choices, default=Labs.NONE)
    matrix = models.CharField(
        max_length=6, choices=Matrices.choices, default=Matrices.NONE)

    class Meta:
        verbose_name = 'characteristic_test_labs'
        verbose_name_plural = 'characteristic_test_labs'

    def __str__(self):
        return '(%s): %s - %s' % (self.pk, self.lab, self.matrix)


class TestLab(models.Model):
    characteristic = models.ForeignKey(
        CharacteristicTestLab, verbose_name='test caracteristic', null=True, blank=True, on_delete=models.CASCADE)
    name_test = models.CharField(max_length=254)
    basic_norm = models.CharField(max_length=254, blank=True, null=True)
    refer_norm = models.CharField(max_length=254, blank=True, null=True)
    unit = models.CharField(
        max_length=10, choices=Unit.choices, default=Unit.NONE)
    quantity = models.PositiveSmallIntegerField(
        default=1)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    is_parent = models.BooleanField(default=False)
    created = models.DateTimeField(
        verbose_name='created at', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='updated at', auto_now=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'test_lab'
        verbose_name_plural = 'tests_labs'

    def __str__(self):
        return '(%s): %s' % (self.pk, self.name_test)


class TestInclude(models.Model):
    to_test = models.ForeignKey(
        TestLab, on_delete=models.CASCADE, related_name='to_test')
    from_test = models.ForeignKey(
        TestLab, on_delete=models.CASCADE, related_name='from_test')

    def __str__(self):
        return '(%s): (%s) - (%s)' % (self.pk, self.to_test, self.from_test)
