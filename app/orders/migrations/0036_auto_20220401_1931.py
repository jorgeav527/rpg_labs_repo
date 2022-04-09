# Generated by Django 3.2 on 2022-04-02 00:31

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('members', '0003_auto_20220324_1202'),
        ('companies', '0002_company_type_company'),
        ('tests_labs', '0004_alter_testlab_unit'),
        ('orders', '0035_auto_20220401_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'order execution',
                'verbose_name_plural': 'orders execution',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='OrderQuatotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quatotion', models.BooleanField(default=True)),
                ('requirement', models.BooleanField(default=True)),
                ('execution', models.BooleanField(default=False)),
                ('liquidation', models.BooleanField(default=False)),
                ('type_service', models.CharField(choices=[('TEST', 'Ensayo'), ('SOIL_MECHANICS_STUDY', 'Estudio de Mecánica de Suelos'), ('GEOTECHNICS_STYDY', 'Estudio de Geotécnico')], default='TEST', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('client', smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='company', chained_model_field='company', null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.clientprofile', verbose_name='client_order')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.company', verbose_name='company_order')),
                ('project', smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='company', chained_model_field='company', null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project', verbose_name='project_order')),
            ],
            options={
                'verbose_name': 'order quatotion',
                'verbose_name_plural': 'orders quatotion',
                'ordering': ('-pk',),
            },
        ),
        migrations.RemoveField(
            model_name='orderquatition',
            name='client',
        ),
        migrations.RemoveField(
            model_name='orderquatition',
            name='company',
        ),
        migrations.RemoveField(
            model_name='orderquatition',
            name='project',
        ),
        migrations.RemoveField(
            model_name='orderitemquatotion',
            name='characteristictestlab',
        ),
        migrations.RemoveField(
            model_name='orderitemquatotion',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitemquatotion',
            name='test_lab',
        ),
        migrations.AddField(
            model_name='orderitemquatotion',
            name='characteristic_testlab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.characteristictestlab', verbose_name='characteristic testlab'),
        ),
        migrations.AddField(
            model_name='orderitemquatotion',
            name='testlab',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='characteristic_testlab', chained_model_field='characteristic', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests_labs.testlab', verbose_name='testlab'),
        ),
        migrations.DeleteModel(
            name='OrderItemLiquidation',
        ),
        migrations.AddField(
            model_name='orderexecution',
            name='order_quatotion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.orderquatotion'),
        ),
        migrations.AddField(
            model_name='orderitemquatotion',
            name='order_quatotion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orderquatotion', verbose_name='order quatotion'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.orderquatotion'),
        ),
        migrations.AlterField(
            model_name='orderitemexecution',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orderquatotion', verbose_name='order'),
        ),
        migrations.DeleteModel(
            name='OrderQuatition',
        ),
    ]