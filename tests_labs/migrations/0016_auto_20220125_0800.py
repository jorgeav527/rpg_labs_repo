# Generated by Django 3.2 on 2022-01-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0015_auto_20220124_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testlab',
            name='is_child',
        ),
        migrations.AddField(
            model_name='testlab',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
    ]