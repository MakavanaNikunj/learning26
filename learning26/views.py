from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render

#function ne call karava mate function related specific url banavi pade
def test(request):
    return HttpResponse("Hello")

# def AboutUse(reqest):
#      return HttpResponse("About")


def AboutUse(reqest):
    return render(reqest,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")

def movies(request):
    return render(request,"movies.html")

def news(request):
    return render(request,"news.html")

def shows(request):
    return render(request,"shows.html")

def gaming(request):
    return render(request,"gaming.html")

def recipe(request):
    ingredient = ["maggie","tomato"]
    data = {"name":"maggie","time":20, "ingredient" : ingredient}   
    return render(request,"recipe.html",data)

def team(request):
    team = ["csk"]
    player = ["ms dhoni","virat kohli","sachin tedulkar"]
    data = {"captain":"virat kohli","trophy": 4,"player" : player,"team" :team}
    return render(request,"team.html",data)

def animal(request):
    animal = ["elephant","labour","jiraf","dog","lapard","etc"]
    data = {"Dangeranimal": "lion" ,"animal" : animal}
    return render(request,"animal.html",data)