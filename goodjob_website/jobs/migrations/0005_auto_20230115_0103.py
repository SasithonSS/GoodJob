# Generated by Django 3.1.5 on 2023-01-14 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20230115_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='score',
        ),
        migrations.AddField(
            model_name='job',
            name='jobber_score',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.score'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobber',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]