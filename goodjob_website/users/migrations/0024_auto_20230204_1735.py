# Generated by Django 3.1.5 on 2023-02-04 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_auto_20230204_1538'),
        ('users', '0023_auto_20230203_0437'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobUser',
            new_name='Job',
        ),
    ]
