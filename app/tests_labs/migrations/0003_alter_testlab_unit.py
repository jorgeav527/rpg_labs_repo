# Generated by Django 3.2 on 2022-03-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0002_alter_testlab_characteristic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testlab',
            name='unit',
            field=models.CharField(choices=[('None', '--------'), ('UND', 'Und.'), ('NOCHE', 'noche'), ('DIA', 'día'), ('PROBETA', 'probeta')], default='None', max_length=10),
        ),
    ]