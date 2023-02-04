from django.db import models

# Create your models here.
class Province(models.Model):
    province = models.CharField('จังหวัด',max_length=100)

    def __str__(self):
        return self.province

class Gender(models.Model):
    gender = models.CharField('เพศ',max_length=100)

    def __str__(self):
        return self.gender

class Education(models.Model):
    education = models.CharField('ระดับการศึกษา',max_length=100)

    def __str__(self):
        return self.education

class Pay(models.Model):
    pay = models.CharField('ค่าตอบแทน',max_length=100)

    def __str__(self):
        return self.pay

class JobberSubjectComplain(models.Model):
    subject = models.CharField('หัวข้อร้องเรียน',max_length=100)

    def __str__(self):
        return self.subject

class EmployerSubjectComplain(models.Model):
    subject = models.CharField('หัวข้อร้องเรียน',max_length=100)

    def __str__(self):
        return self.subject


