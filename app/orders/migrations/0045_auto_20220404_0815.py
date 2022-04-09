# Generated by Django 3.2 on 2022-04-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0044_alter_orderliquidation_order_execution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitemliquidation',
            old_name='order_execution',
            new_name='order_liquidation',
        ),
        migrations.AlterField(
            model_name='orderitemliquidation',
            name='sampling_by',
            field=models.CharField(choices=[('N/A', 'N/A'), ('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=4),
        ),
    ]