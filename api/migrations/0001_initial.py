# Generated by Django 3.2 on 2022-01-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(default=0)),
                ('task', models.CharField(max_length=255)),
                ('status', models.BooleanField(max_length=1)),
            ],
        ),
    ]
