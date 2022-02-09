# Generated by Django 3.2 on 2022-02-06 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orderitems_characteristictestlab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.order', verbose_name='order'),
        ),
    ]
