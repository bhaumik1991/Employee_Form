from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from emp.models import Employee
from .forms import EmployeeForm

def preview(request):
    employees = Employee.objects.all()
    return render(request, 'welcome.html',{'employees':employees})


def profile(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'profile.html', {'form':form})

def deleteEmployee(request, pk):
    if request.method == 'POST':
        profile = Employee.objects.get(pk=pk)
        profile.delete()
    return redirect('employee_list')

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'profile.html'
    fields = ['full_name','gender','salary','occupation']
    success_url = reverse_lazy('employee_list')

