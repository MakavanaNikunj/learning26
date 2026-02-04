from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.studentHome),
    path("dashboard/",views.studentDashboard),
    path("data/",views.studentData),
    path("fruits/",views.fruits),
    path("birds/",views.birds),
    path("gods/",views.gods)
    
]
