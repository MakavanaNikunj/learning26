from django import forms
from .models import Employee,Course,StudentProfile1,Animal


#employee forms
#models form --> it will create using model fields

class EmployeeForm(forms.ModelForm):
    class Meta:
       model = Employee
       fields = '__all__' 


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields ='__all__'  


class StudentForm(forms.ModelForm):
    class Meta:
        model= StudentProfile1
        fields = '__all__'    


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'                   





     
