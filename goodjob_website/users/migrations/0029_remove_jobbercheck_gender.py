# Generated by Django 3.1.5 on 2023-02-07 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_jobberuser_hasjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobbercheck',
            name='gender',
        ),
    ]
