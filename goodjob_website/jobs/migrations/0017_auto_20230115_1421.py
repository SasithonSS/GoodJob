# Generated by Django 3.1.5 on 2023-01-15 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_auto_20230115_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobber',
            name='age',
            field=models.IntegerField(default=0, verbose_name='อายุ'),
        ),
    ]