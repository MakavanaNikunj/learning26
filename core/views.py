from django.shortcuts import render,redirect
from.forms import UserForm
from.models import User

# Create your views here.
def registerUser(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("employeeList")

    else:
        return render(request, "core/register.html", {"form": form})        


