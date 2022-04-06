# Generated by Django 3.2 on 2022-03-27 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_alter_question_orderinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='question',
            name='obs',
        ),
        migrations.RemoveField(
            model_name='question',
            name='orderinfo',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='question',
            field=models.ManyToManyField(blank=True, to='orders.Question', verbose_name='questions'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.BooleanField(null=True)),
                ('obs', models.TextField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.question')),
            ],
        ),
    ]
