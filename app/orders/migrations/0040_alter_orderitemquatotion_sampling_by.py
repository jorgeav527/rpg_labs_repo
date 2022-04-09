# Generated by Django 3.2 on 2022-04-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0039_alter_orderitemquatotion_sampling_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemquatotion',
            name='sampling_by',
            field=models.CharField(choices=[('None', 'N/A'), ('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=4),
        ),
    ]