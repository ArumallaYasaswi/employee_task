from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import Employeeform
from django.urls import reverse

# url = reverse('crud:employee_create')


# Create your views here.
def employee_list(request):
    employee = Employee.objects.all() 
    return render(request, "crud/employee_list.html", {"employees": employee})

def employee_create(request):
    if request.method == "POST":
        form = Employeeform(request.POST, request.FILES)
        print("form", form)
        if form.is_valid():
            form.save()
            print("formsave")
            return redirect("employee_list")
    else:
        form = Employeeform()
        print("formelse", form)
    return render(request, "crud/employee_form.html",{"form": form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = Employeeform(request.POST, request.FILES, instance = employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = Employeeform(instance = employee)
    return render(request, "crud/employee_form.html", {"form": form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")
    return render(request, "crud/employee_confirm_delete.html", {"employee": employee})