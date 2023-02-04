# Generated by Django 3.1.5 on 2023-01-26 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('jobs', '0019_auto_20230115_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobberUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='ชื่อผู้ใช้')),
                ('name', models.CharField(max_length=100, verbose_name='ชื่อ-สกุล')),
                ('email', models.EmailField(max_length=100, verbose_name='อีเมล')),
                ('phone', models.CharField(max_length=100, verbose_name='เบอร์โทร')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='ที่อยู่')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='ที่ตั้ง')),
                ('age', models.IntegerField(default=0, verbose_name='อายุ')),
                ('picture', models.FileField(blank=True, null=True, upload_to='jobs/static/jobs/images/Jobber/', verbose_name='รูปภาพ')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.education', verbose_name='ระดับการศึกษา')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.gender')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.province', verbose_name='จังหวัด')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='ชื่อผู้ใช้')),
                ('name', models.CharField(max_length=100, verbose_name='ชื่อองค์กร/ร้านค้า')),
                ('emp_name', models.CharField(max_length=100, verbose_name='ชื่อผู้จ้าง')),
                ('email', models.EmailField(max_length=100, verbose_name='อีเมล')),
                ('phone', models.CharField(max_length=100, verbose_name='เบอร์โทร')),
                ('address', models.CharField(max_length=100, verbose_name='ที่อยู่')),
                ('location', models.CharField(max_length=100, verbose_name='ที่ตั้ง')),
                ('picture', models.FileField(blank=True, null=True, upload_to='jobs/static/jobs/images/Employer/', verbose_name='รูปภาพ')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.province', verbose_name='จังหวัด')),
            ],
        ),
    ]
