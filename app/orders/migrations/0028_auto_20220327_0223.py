# Generated by Django 3.2 on 2022-03-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='question',
            name='orderinfo',
        ),
        migrations.AddField(
            model_name='question',
            name='orderinfo',
            field=models.ManyToManyField(to='orders.OrderInfo', verbose_name='questions'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
