# Generated by Django 3.2 on 2022-03-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_orderitem_obs'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='unit',
            field=models.CharField(choices=[('None', 'Escoja la unidad'), ('UND', 'Und.'), ('NOCHE', 'noche'), ('DIA', 'día'), ('PROBETA', 'probeta')], default='None', max_length=10),
        ),
    ]