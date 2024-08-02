from django.shortcuts import render, redirect
from . import forms 

# Create your views here.


def add_category(request):
    if request.method == 'POST':
        category = forms.Cat_Form(request.POST)
        if category.is_valid():
            category.save()
            return redirect('category')
    else:
        category = forms.Cat_Form()
    return render(request, 'cat.html', {'cat':category})

