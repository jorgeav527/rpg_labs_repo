# Generated by Django 3.2 on 2022-03-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_alter_question_orderinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='orderinfo',
            field=models.ManyToManyField(blank=True, to='orders.OrderInfo', verbose_name='questions'),
        ),
    ]
