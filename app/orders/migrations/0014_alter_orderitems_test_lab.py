# Generated by Django 3.2 on 2022-03-16 21:48

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0002_alter_testlab_characteristic'),
        ('orders', '0013_alter_orderitems_test_lab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='test_lab',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='characteristictestlab', chained_model_field='characteristic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.testlab', verbose_name='test lab'),
        ),
    ]
