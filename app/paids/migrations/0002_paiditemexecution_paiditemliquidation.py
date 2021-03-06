# Generated by Django 3.2 on 2022-04-05 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0046_orderliquidation_observation'),
        ('paids', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaidItemLiquidation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_liquidation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orderliquidation', verbose_name='paid liquidation')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='PaidItemExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_execution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orderexecution', verbose_name='paid execution')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
