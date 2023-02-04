# Generated by Django 3.1.5 on 2023-01-15 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20230115_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.province', verbose_name='จังหวัด'),
        ),
        migrations.AlterField(
            model_name='jobber',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.province', verbose_name='จังหวัด'),
        ),
    ]
