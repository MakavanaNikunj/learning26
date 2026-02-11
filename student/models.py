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

    def __str__(self):
       return self.studentName

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
    def __str__(self):
        return self.productName    

class Electronics(models.Model):
    electricMachineName = models.CharField(max_length=20)
    electricMachinePrice = models.IntegerField()
    electricMachineStock = models.PositiveIntegerField()
    electricMachineWarranty = models.PositiveIntegerField()


    #meta class
    class Meta:
        db_table = "electronicMachine"

    def __str__(self):
        return self.electricMachineName  


    #one to one table means one student belong one profile   

class StudentProfile(models.Model):
    hobbies = (("reading","Reading"),("travel","Travel"),("music","Music" ))
    #StudentProfile ni id jate create thashe and e primary key as
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()    

    class Meta:
        db_table = "studentprofile"

    def __str__(self):
       return self.studentId.studentName
    


#one to many relationship 
#category ---> #service  category one is provided many service of the customer



class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True) 


    class Meta:
      db_table = "category"

    def __str__(self):
        return self.categoryName  
    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDiscription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    descount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)


    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName   


    

        


