from django.shortcuts import render,HttpResponse
from .models import Employee
from .forms import EmployeeForm

# Create your views here.


def employeeList(request):
    employees = Employee.objects.all()             # select * from employee work as
    employees = Employee.objects.all().values()   # object ni values aape 
    print(employees)
    employees = Employee.objects.all().values_list()   
    print(employees)
    return render(request,"employee/employeeList.html",{"employees":employees})

def employeeFilter(request):
    employee1 = Employee.objects.filter(name = "raj").values()
    print("query1", employee1)
    employee2 = Employee.objects.filter(post ="Developer").values()
    print("query2", employee2)
    employee3 = Employee.objects.filter(name = "raja",post = "Developer").values()
    print("query3",employee3)

    employee4 = Employee.objects.filter(age__gt=23).values()
    print("query4",employee4)
    employee5 = Employee.objects.filter(age__gte=23).values()
    print("query5",employee5)

    employee6 = Employee.objects.filter(age__lt=30).values()
    print("query6",employee6)



    #string queries
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    print("query6",employee6)
    employee6 = Employee.objects.filter(post__iexact="developer").values()
    print("query6",employee6)


    #contains queris
    employee8 = Employee.objects.filter(name__contains="r").values()
    print("query8",employee8)
    employee8 = Employee.objects.filter(name__icontains="j").values()
    # print("query8",employee8)


    #startwith && ends with 
    employee9 = Employee.objects.filter(name__startswith="j").values()
    # print("query9",employee9)
    employee9 = Employee.objects.filter(name__istartswith="R").values()
    # print("query9",employee9)

    #ensd with
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
      
      Employee.objects.create(name="ajay",age=23,salary=23000,post="HR",join_date ="2022-01-01")

      return HttpResponse("employee created...")

      return render(request,'employee/employeeFilter.html')

def createEmployeeWithForm(request):
      print(request.method)
      if request.method == "POST":
           form = EmployeeForm(request.POST)
           if form.is_valid():
                form.save()
                return HttpResponse("Employee is Created...")
      else:
           form = EmployeeForm()
           return render(request,"employee/createEmployeeForm.html",{"form":form})     
         
def createStudent(request):
     Employee.objects.create(name="nikunj",age="21",salary="21000",join_date="2022-2-25",post="Hr")
     
     
     return HttpResponse("student is created....--->")