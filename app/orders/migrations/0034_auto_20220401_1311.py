# Generated by Django 3.2 on 2022-04-01 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_company_type_company'),
        ('members', '0003_auto_20220324_1202'),
        ('projects', '0001_initial'),
        ('orders', '0033_auto_20220327_1123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='OrderQuatition',
        ),
        migrations.AlterField(
            model_name='orderitemexecution',
            name='unit',
            field=models.CharField(choices=[('None', '--------'), ('UND', 'und.'), ('NOCHE', 'noche'), ('DIA', 'día'), ('PROBETA', 'probeta'), ('PUNTO', 'punto'), ('KM/CARRIL', 'km/carril'), ('KM', 'km')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderitemliquidation',
            name='unit',
            field=models.CharField(choices=[('None', '--------'), ('UND', 'und.'), ('NOCHE', 'noche'), ('DIA', 'día'), ('PROBETA', 'probeta'), ('PUNTO', 'punto'), ('KM/CARRIL', 'km/carril'), ('KM', 'km')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderitemquatotion',
            name='unit',
            field=models.CharField(choices=[('None', '--------'), ('UND', 'und.'), ('NOCHE', 'noche'), ('DIA', 'día'), ('PROBETA', 'probeta'), ('PUNTO', 'punto'), ('KM/CARRIL', 'km/carril'), ('KM', 'km')], default='None', max_length=10),
        ),
    ]
