from django import forms
from .models import Employee


#employee forms
#models form --> it will create using model fields

class EmployeeForm(forms.ModelForm):
    class Meta:
       model = Employee
       fields = '__all__'    

     
