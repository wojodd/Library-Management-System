from django.db import models
import datetime
# Create your models here.
class CustomUsers(models.Model):
   Fname = models.CharField(max_length=100)
   Lname = models.CharField(max_length=100)
   Father_name = models.CharField(max_length=100)
   Father_name = models.CharField(max_length=100)
   gender_id=models.ForeignKey(gender,on_delete=models.CASCADE)
   feculty_id=models.ForeignKey(Faculty,on_delete=models.CASCADE)
   semester_id=models.ForeignKey(Semester, on_delete=models.CASCADE)
   email=models.EmailField(max_length=100)
   contant_no=models.IntegerField(max_length=100)
   identification_no=models.IntegerField(max_length=100)
   Registration_no=models.IntegerField(max_length=100)
   page_no=models.IntegerField(max_length=100)
   original_Address=models.CharField(max_length=100)
   current_Address=models.CharField(max_length=100)
   UserName=models.CharField(max_length=100)
   Password=models.CharField(max_length=100)
   role_id=models.ForeignKey(Role, on_delete=models.CASCADE)
   Is_Active=models.SmallIntegerField(auto_increment=True, primary_key=True)
   signature=models.CharField(max_length=100)

class gender(models.Model):
    gender=models.CharField(max_length=100)
    Gender_person=models.CharField(max_length=100)

class Libraries(models.Model):
    feculty_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    Content=models.CharField(max_length=100)
    Content_persain=models.CharField(max_length=100)
    privacy=models.CharField(max_length=100)
    privacy_persain=models.CharField(max_length=100)
    services=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

class Despositves(models.Model):
    User_id=models.ForeignKey(CustomUsers,on_delete=models.CASCADE)
    Copy_id=models.ForeignKey(Copy,on_delete=models.CASCADE)
    issue_date= models.DateField()
    due_date= models.DateField()

class Semester(models.Model):
    semester=models.CharField(max_length=100)
    semester_persain=models.CharField(max_length=100)

class Cities(models.Model):
    city=models.CharField(max_length=100)
    city_persain=models.CharField(max_length=100)

class Role(models.Model):
    role=models.CharField(max_length=100)
    role_persain=models.CharField(max_length=100)