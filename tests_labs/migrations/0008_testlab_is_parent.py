# Generated by Django 3.2 on 2022-01-20 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0007_alter_testlab_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='testlab',
            name='is_parent',
            field=models.BooleanField(default=True),
        ),
    ]
