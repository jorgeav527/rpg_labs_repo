# Generated by Django 3.2 on 2021-12-23 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
