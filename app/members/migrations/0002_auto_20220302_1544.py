# Generated by Django 3.2 on 2022-03-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientprofile',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='adminprofile',
            name='charge',
            field=models.CharField(choices=[('None', 'Ninguna'), ('GT', 'Gerente Técnico'), ('GL', 'Gerente Laboratorio')], default='None', max_length=10),
        ),
    ]
