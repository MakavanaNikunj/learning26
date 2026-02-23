from . import views
from django.urls import path


urlpatterns = [
      path('employeeList/', views.employeeList,name="employeeList"),
      path('employeeFilter/', views.employeeFilter),
      path('createEmployee/', views.createEmployee),
      path('createEmployeeWithForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),
      path('deleteEmployee/<int:id>',views.deleteEmployee,name = "deleteEmployee"),
      path('filterEmployee/',views.filterEmployee,name="filterEmployee"),
      path('sortEmployee/asc/', views.sortEmployeeAsc, name="accending"),
      path('sortEmployee/desc/', views.sortEmployeeDesc, name="deccending"),
      path('createCourse/',views.createCourse,name="createCourse"),
      path('createStudent/',views.createStudent),
      path('createanimal/',views.createAnimal,name="createanimal"),
      path('upateemployee/<int:id>/',views.updateEmployee,name="updateEmployee")
 
]
