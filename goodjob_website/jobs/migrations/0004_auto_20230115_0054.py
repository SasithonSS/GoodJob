# Generated by Django 3.1.5 on 2023-01-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20230115_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.CharField(max_length=4),
        ),
    ]
