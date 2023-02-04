# Generated by Django 3.1.5 on 2023-02-04 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_employersubjectcomplain_jobbersubjectcomplain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='emp_name',
        ),
        migrations.RemoveField(
            model_name='job',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pay',
        ),
        migrations.RemoveField(
            model_name='job',
            name='province',
        ),
        migrations.RemoveField(
            model_name='jobber',
            name='education',
        ),
        migrations.RemoveField(
            model_name='jobber',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='jobber',
            name='province',
        ),
        migrations.RemoveField(
            model_name='location',
            name='province',
        ),
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='Jobber',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
