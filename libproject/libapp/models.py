from django.db import models



# Create your models here.

class Teacher(models.Model):
    fname=models.CharField(max_length=50,null=False)
    lname=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    phone=models.IntegerField(default=0)
    email=models.EmailField(default='abc@xyz.com')

    def __str__(self):
        return '%s %s' %(self.fname,self.lname)

class Student(models.Model):
    fname=models.CharField(max_length=50,null=False)
    lname=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    phone=models.IntegerField(default=0)
    email=models.EmailField(default='abc@xyz.com')

    def __str__(self):
        return '%s %s' %(self.fname,self.lname)

class Books(models.Model):
    bid=models.IntegerField(default=0,null=False)
    bname=models.CharField(max_length=100,null=False)
    author=models.CharField(max_length=100)
    publication=models.CharField(max_length=100)
    price=models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' %(self.bid,self.bname)
