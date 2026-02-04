from django.shortcuts import render

# Create your views here.

def studentHome(request):
    return render(request,"student/studentHome.html")

def studentDashboard(request):
    return render(request,"student/studentDashboard.html")

def studentData(request):
    data = {"name":"nikunj","age":21,"city":"Ahmedabad","xender":"male"}
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