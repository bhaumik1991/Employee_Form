from django import forms
from emp.models import Employee

GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ]
OCCUPATION_CHOICES = [
    ('select', 'Select'),
    ('Software Developer', 'Software Developer'),
    ('HR', 'HR'),
]
class EmployeeForm(forms.ModelForm):
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_CHOICES))
    occupation = forms.CharField(widget=forms.Select(choices=OCCUPATION_CHOICES))
    full_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[A-Za-z ]+',
               'title': 'Enter Characters Only '}))

    class Meta:
        model=Employee
        fields = ['full_name','gender', 'salary', 'occupation']

