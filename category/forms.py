from django import forms 
from . models import TaskCategory


class Cat_Form(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'
        

        