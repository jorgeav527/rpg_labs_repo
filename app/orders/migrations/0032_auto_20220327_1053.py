# Generated by Django 3.2 on 2022-03-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20220327_1030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfo',
            name='question',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question_1',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question_2',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question_3',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question_4',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question_5',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question_6',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question_7',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question_8',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]