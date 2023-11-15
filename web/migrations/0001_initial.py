# Generated by Django 4.2.2 on 2023-11-09 09:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabourUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('userId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('password', models.CharField(max_length=10)),
                ('profession', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=10)),
                ('mobile', models.IntegerField()),
                ('excperience', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=10)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]