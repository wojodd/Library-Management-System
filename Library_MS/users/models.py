from django.db import models
from books.models import *
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Semester(models.Model):
    semester=models.CharField(max_length=100)
    semester_persain=models.CharField(max_length=100)

class Cities(models.Model):
    city=models.CharField(max_length=100)
    city_persain=models.CharField(max_length=100)

class Role(models.Model):
    role=models.CharField(max_length=100)
    role_persain=models.CharField(max_length=100)
    
class gender(models.Model):
    gender=models.CharField(max_length=100)
    Gender_person=models.CharField(max_length=100)
    
class CustomUsers(AbstractUser):
    Father_name = models.CharField(max_length=100)
    gender_id=models.ForeignKey(gender,on_delete=models.CASCADE,null=True)
    feculty_id=models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True)
    semester_id=models.ForeignKey(Semester,on_delete=models.CASCADE,null=True)
    contant_no=models.CharField(max_length=14)
    Registration_no=models.IntegerField(null=True)
    original_Address=models.CharField(max_length=100)
    current_Address=models.CharField(max_length=100)
    role_id=models.ForeignKey(Role,on_delete=models.CASCADE, null=True)
    signature=models.CharField(max_length=100)



    class Meta:
        db_table = 'auth_user'

class Despositves(models.Model):
    User_id=models.ForeignKey(CustomUsers,on_delete=models.CASCADE)
    Copy_id=models.ForeignKey(Copy,on_delete=models.CASCADE)
    issue_date= models.DateField()
    due_date= models.DateField()