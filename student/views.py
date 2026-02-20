from django.shortcuts import render,redirect
from .models import Service
from .forms import ServiceForm

# Create your views here.

def studentHome(request):
    return render(request,"student/studentHome.html")

def studentDashboard(request):
    return render(request,"student/studentDashboard.html")

def studentData(request):
    data = {"name":"nikunj","age":21,"city":"Ahmedabad","gender":"male"}
    return render(request,"student/studentData.html",data)


def fruits(request):
    data = {"smallfruits":"grapes","bigfruits":"watermelon"}
    return render(request,"student/fruits.html",data)

def birds(request):
    birdsdata = {"bigbirds":"peacock","smallbirds":"spaprow"}
    return render(request,"student/birds.html",birdsdata)

def gods(request):
    godName = {"dwrkatempe":"krishna(DWRKADHISH)","girnar":"mahadev"}
    return render(request,"student/god.html",godName)

def serviceList(request):
    services = Service.objects.all()
    return render(request,"student/serviceList.html",{"services":services})

def createService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createService.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"student/createService.html",{"form":form})
    
def deleteService(request, id):
    service = Service.objects.get(id=id)
    if request.method == "POST":
        service.delete()
        return redirect("serviceList")
