# Generated by Django 3.2 on 2022-01-22 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0013_auto_20220122_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteristictestlab',
            options={'verbose_name': 'characteristic_test_labs', 'verbose_name_plural': 'characteristic_test_labs'},
        ),
        migrations.AlterModelOptions(
            name='testlab',
            options={'ordering': ('created',), 'verbose_name': 'test_lab', 'verbose_name_plural': 'tests_labs'},
        ),
        migrations.RemoveField(
            model_name='characteristictestlab',
            name='created',
        ),
        migrations.RemoveField(
            model_name='characteristictestlab',
            name='updated',
        ),
        migrations.AddField(
            model_name='testlab',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testlab',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated at'),
        ),
    ]