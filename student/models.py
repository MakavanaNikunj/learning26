from django.db import models

# Create your models here.


class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)


    #meta class
    class Meta:
        db_table = "student"

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDiscription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    produtStatus = models.BooleanField(default=True)

    
    #meta class
    class Meta:
        db_table = "product"

class Electronics(models.Model):
    electricMachineName = models.CharField(max_length=20)
    electricMachinePrice = models.IntegerField()
    electricMachineStock = models.PositiveBigIntegerField()
    electricMachineWarranty = models.PositiveBigIntegerField()


    #meta class
    class Meta:
        db_table = "electronicMachine"


    

        


