from django.db import models
from django.contrib.auth.models import User

# Create your models here.(
class S_user(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    types=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.user.first_name

class Placed_student(models.Model):
    image=models.FileField(null=True)
    company=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.company

class Recruiter(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    company=models.CharField(max_length=100,null=True)
    types=models.CharField(max_length=10,null=True)
    status=models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.company

class AddJob(models.Model):
    recruiter=models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    title=models.CharField(max_length=20)
    salary=models.FloatField(max_length=20)
    image=models.FileField(null=True)
    description=models.TextField(max_length=500,null=True)
    experience=models.CharField(max_length=50,null=True)
    Location=models.CharField(max_length=50,null=True)
    skills=models.TextField(max_length=500,null=True)
    creationdate=models.DateField()
    def __str__(self):
        return self.title
