from django.db import models

# Create your models here.



class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField(auto_now_add=True)
    post = models.CharField(max_length=20)

    #class meta
    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.name
    
class  Course(models.Model):
    name = models.CharField(max_length=20)
    duration = models.IntegerField()
    fees = models.IntegerField()

    class Meta:
        db_table="course"

    def __str__(self):
        return self.name  

class StudentProfile1(models.Model):
    hobbies=(("playing","playing"),("study","study"),("working","working"))
    name = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    addres=models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    hobbies=models.CharField(max_length=100,choices=hobbies)

    class Meta:
        db_table = "studentprofile1"

    def __str__(self):
        return self.name    
    

class Animal(models.Model):
    flying = (("yes","yes"),("No","No"))
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    eating = models.CharField(max_length=20)
    flying = models.CharField(max_length=20,choices=flying)


    class Meta:
        db_table = "animal"

    def __str__(self):
        return self.name    

        



