# Generated by Django 3.2 on 2022-03-26 15:41

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0003_alter_testlab_unit'),
        ('orders', '0022_alter_order_requirement'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItemLiquidation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(choices=[('None', '--------'), ('UND', 'Und.'), ('NOCHE', 'noche'), ('DIA', 'día'), ('PROBETA', 'probeta')], default='None', max_length=10)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sampling_by', models.BooleanField(null=True)),
                ('obs', models.TextField(blank=True, null=True)),
                ('characteristictestlab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.characteristictestlab', verbose_name='characteristictestlab')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='order')),
                ('test_lab', smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='characteristictestlab', chained_model_field='characteristic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.testlab', verbose_name='test lab')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
