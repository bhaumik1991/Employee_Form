import re
from django import forms
from emp.models import Employee
from django.core.files.images import get_image_dimensions

GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ]
STATUS_CHOICES=[('enable','Enable'),
         ('disable','Disable')]
class EmployeeForm(forms.ModelForm):
    gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)
    full_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[A-Za-z ]+',
               'title': 'Enter Characters Only '}))

    class Meta:
        model=Employee
        fields = ['full_name','email', 'image', 'gender', 'status']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError("Invalid Email")
        return email
    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            raise forms.ValidationError("no image")
        else:
            w, h = get_image_dimensions(image)
            if w != 500:
                raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 500px" % w)
            if h != 700:
                raise forms.ValidationError("The image is %i pixel height. It's supposed to be 700px" % h)
        return image


