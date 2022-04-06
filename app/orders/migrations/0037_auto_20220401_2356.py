# Generated by Django 3.2 on 2022-04-02 04:56

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0004_alter_testlab_unit'),
        ('orders', '0036_auto_20220401_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemexecution',
            name='characteristictestlab',
        ),
        migrations.RemoveField(
            model_name='orderitemexecution',
            name='obs',
        ),
        migrations.RemoveField(
            model_name='orderitemexecution',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitemexecution',
            name='test_lab',
        ),
        migrations.AddField(
            model_name='orderitemexecution',
            name='characteristic_testlab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.characteristictestlab', verbose_name='characteristic testlab'),
        ),
        migrations.AddField(
            model_name='orderitemexecution',
            name='order_execution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orderexecution', verbose_name='order execution'),
        ),
        migrations.AddField(
            model_name='orderitemexecution',
            name='testlab',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='characteristic_testlab', chained_model_field='characteristic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.testlab', verbose_name='test lab'),
        ),
        migrations.CreateModel(
            name='OrderLiquidation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('order_execution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderexecution')),
            ],
            options={
                'verbose_name': 'order liquidation',
                'verbose_name_plural': 'orders liquidation',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='OrderItemLiquidation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('None', '--------'), ('UND', 'und.'), ('NOCHE', 'noche'), ('DIA', 'día'), ('PROBETA', 'probeta'), ('PUNTO', 'punto'), ('KM/CARRIL', 'km/carril'), ('KM', 'km')], default='None', max_length=10)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sampling_by', models.BooleanField(null=True)),
                ('characteristic_testlab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.characteristictestlab', verbose_name='characteristic testlab')),
                ('order_execution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orderliquidation', verbose_name='order liquidation')),
                ('testlab', smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='characteristic_testlab', chained_model_field='characteristic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.testlab', verbose_name='testlab')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
