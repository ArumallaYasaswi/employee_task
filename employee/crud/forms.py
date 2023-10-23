from django import forms
from .models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id','Name', 'Email', 'PhoneNo', 'Country', 'Address', 'Gender', 'Image']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Employee.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
