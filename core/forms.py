#django built in table means Absract base User
from django.contrib.auth.forms import UserCreationForm
from.models import User



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','role','password1','password2']
