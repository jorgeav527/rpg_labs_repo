# Generated by Django 3.2 on 2022-04-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0040_alter_orderitemquatotion_sampling_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderquatotion',
            name='observation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderitemquatotion',
            name='sampling_by',
            field=models.CharField(choices=[('N/A', 'N/A'), ('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=4),
        ),
    ]
