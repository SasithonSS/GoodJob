# Generated by Django 3.1.5 on 2023-01-31 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20230201_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employercheck',
            name='age',
        ),
        migrations.RemoveField(
            model_name='employercheck',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='jobbercheck',
            name='age',
        ),
        migrations.RemoveField(
            model_name='jobbercheck',
            name='gender',
        ),
    ]
