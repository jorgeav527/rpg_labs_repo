# Generated by Django 3.2 on 2022-01-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0004_alter_testlab_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testlab',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]
