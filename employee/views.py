from django.shortcuts import render,HttpResponse,redirect

from .models import Employee
from .forms import EmployeeForm,CourseForm,StudentForm,AnimalForm

# Create your views here.


def employeeList(request):
    employees1 = Employee.objects.all() # select * from employee work as
    # print(employees1)                     
    employees = Employee.objects.all().values()   # object ni values aape key value pair
#     print(employees)
#     employees3 = Employee.objects.all().values_list()   
#     print(employees3)
    return render(request,"employee/employeeList.html",{"employees":employees})

def employeeFilter(request):
    employee1 = Employee.objects.filter(name = "raj").values()
#     print("query1", employee1)
    employee2 = Employee.objects.filter(post ="Developer").values()
    # print("query2", employee2)
    employee3 = Employee.objects.filter(name = "raja",post = "Developer").values()
    # print("query3",employee3)

    employee4 = Employee.objects.filter(age__gt=23).values()
    # print("query4",employee4)
    employee5 = Employee.objects.filter(age__gte=23).values()
    # print("query5",employee5)

    employee6 = Employee.objects.filter(age__lt=30).values()
    # print("query6",employee6)



    #string queries
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    # print("query6",employee6)
    employee6 = Employee.objects.filter(post__iexact="developer").values()
    # print("query6",employee6)


    #contains queris
    employee8 = Employee.objects.filter(name__contains="r").values()
    # print("query8",employee8)
    employee8 = Employee.objects.filter(name__icontains="j").values()
    # print("query8",employee8)


    #startwith && ends with 
    employee9 = Employee.objects.filter(name__startswith="j").values()
    # print("query9",employee9)
    employee9 = Employee.objects.filter(name__istartswith="R").values()
    # print("query9",employee9)

    #ends with
    employee10 = Employee.objects.filter(name__endswith="y").values()
    # print("query10",employee10)
    employee10 = Employee.objects.filter(name__iendswith="J").values()
    # print("query10",employee10)

    #in quiries
    employee11 = Employee.objects.filter(name__in=["raj","ravi"]).values()
    # print("query11",employee11)
    employee11 = Employee.objects.filter(name__in=["raj","jay"]).values()
    # print("query11",employee11)


    #range quiries
    employee12 = Employee.objects.filter(age__range=[23,30]).values()
    # print("query12",employee12)
    employee12 = Employee.objects.filter(age__range=[23,24]).values()
    # print("query12",employee12)

    #order by quiries
    employee13 = Employee.objects.order_by("age").values()
    # print("query13",employee13)

    employee13 = Employee.objects.order_by("-salary").values()
    # print("query13",employee13)

def createEmployee(request):  
      Employee.objects.create(name="Ajay",age=25,salary=23000,post="Frontend Devloper",join_date ="2022-01-01")
      Employee.objects.create(name="Ram",age=24,salary=2000,post="Backend Devloper",join_date ="2022-01-05")
      Employee.objects.create(name="Arya",age=23,salary=45000,post="FullStack Devploper",join_date ="2022-01-05")

      Employee.objects.create(name="Ajay",age=40,salary=40000,post="Python Devloper",join_date ="2026-01-01")
      Employee.objects.create(name="Ram",age=41,salary=42000,post="Web Devloper",join_date ="2025-01-05")
      Employee.objects.create(name="Arya",age=42,salary=35000,post="PHP Devploper",join_date ="2024-01-05")
      Employee.objects.create(name="Mohan",age=43,salary=45000,post="Frontend Devloper",join_date ="2023-01-01")
      Employee.objects.create(name="Vijay",age=44,salary=44000,post="Backend Devloper",join_date ="2022-01-05")
      Employee.objects.create(name="Sujal",age=45,salary=41000,post="FullStack Devploper",join_date ="2021-01-05")

      return HttpResponse("employee created...")

      return render(request,'employee/employeeFilter.html')

def createEmployeeWithForm(request):
     #  print(request.method)
      if request.method == "POST":
           form = EmployeeForm(request.POST)
           if form.is_valid():
                form.save()
                return HttpResponse("Employeeform is Created...")
      else:
           form = EmployeeForm()
           return render(request,"employee/createEmployeeForm.html",{"form":form})     
         


def deleteEmployee(request,id):
     
     # print("id from url = ",id)       
     Employee .objects.filter(id=id).delete()
     return redirect(employeeList)

def filterEmployee(request):
     # print("filter employee called...-->>")
     employees = Employee.objects.filter(age__gte=25).values()
     # print("filter employee is called...___>>>",employees)
     return render(request,"employee/employeeList.html",{"employees":employees})


def sortEmployeeAsc(request):
     # print("filter in accending order employee using age....>>>")
     employees = Employee.objects.all().order_by("age").values()
     # print("filter employee is called...___>>>",employees)
     return render(request,"employee/employeeList.html",{"employees":employees})



def sortEmployeeDesc(request):
     # print("filter in decending order employee using age....>>>")
     employees = Employee.objects.all().order_by("-age").values()
     # print("filter employee is called...___>>>",employees)
     return render(request,"employee/employeeList.html",{"employees":employees})


def updateEmployee(request,id):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(instance=employee)
        if request.method == "POST":
            form = EmployeeForm(request.POST,instance=employee)
            form.save()
            return redirect(employeeList)
        else:
            return render(request,"employee/updateemployee.html",{"form":form})


def createCourse(request):
     if request.method == "POST":
       form = CourseForm(request.POST)
       if form.is_valid():
            form.save()
            return HttpResponse("corse form  is successfully filled")
     else:
          form = CourseForm()
          return render(request,"employee/createcourse.html",{"form":form})
     

def createStudent(request):
     if request.method =="POST":
       form = StudentForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponse("Student From Succesfully")
     else:
          form = StudentForm()
          return render(request,"employee/createstudent.html",{"form":form})
     

def createAnimal(request):
     if request.method =="POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
             form.save()
             return HttpResponse("Ainimal Form Is Created")
     

     else:
          form = AnimalForm()
          return render(request,"employee/createanimal.html",{"form":form})   
                 




