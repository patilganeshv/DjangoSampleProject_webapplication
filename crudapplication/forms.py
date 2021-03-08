from django import forms
from crudapplication.models import *

class EmployeeForm(forms.ModelsForm):
	class Meta:
		model = Employee
		fields = "__all__"
