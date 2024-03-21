from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    Course_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Course_name
    
    
class Question(models.Model):
    Course =models.ForeignKey(Course,on_delete=models.CASCADE)  
    question=models.CharField(max_length=300)
    answer=models.IntegerField(max_length=200)
    option_one=models.CharField(max_length=200)
    option_two=models.CharField(max_length=200)
    option_three=models.CharField(max_length=200,blank=True)
    option_four=models.CharField(max_length=200,blank=True)
    
    
    marks =models.IntegerField(default=5)
    
    
    def __str__(self):
        return self.question
      
class ScoreBoard(models.Model):
    course  =models.ForeignKey(Course,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score =models.IntegerField()      
   
      