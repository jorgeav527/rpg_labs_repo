# Generated by Django 3.2 on 2022-01-24 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests_labs', '0014_auto_20220122_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testlab',
            name='child_tests',
        ),
        migrations.CreateModel(
            name='TestFriendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_test_friends', to='tests_labs.testlab')),
                ('to_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_test_friends', to='tests_labs.testlab')),
            ],
        ),
    ]
