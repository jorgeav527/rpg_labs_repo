# Generated by Django 3.2 on 2022-03-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_orderitemliquidation'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_execution',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='created_liquidation',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='created_quatotion',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
