# Generated by Django 3.2 on 2022-02-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20220207_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='execution_order',
            field=models.BooleanField(default=False),
        ),
    ]
