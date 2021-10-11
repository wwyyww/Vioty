# Generated by Django 3.1.3 on 2021-10-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20211004_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32, unique=True)),
                ('tel', models.CharField(max_length=32, unique=True)),
                ('agency', models.CharField(max_length=32)),
            ],
        ),
    ]
