from django.shortcuts import render, redirect
from . import forms
from .models import TaskModel
from . import models


def add_task(request):
    if request.method == 'POST':
        task = forms.Tas_Form(request.POST)
        if task.is_valid():
            task.save()
            return redirect('task')
    else:
        task = forms.Tas_Form()
    return render(request, 'tas.html', {'tsk':task})


def see_task(request):
    task = TaskModel.objects.all()
    return render(request, 'home.html', {'task':task})



def edit(request, id):
    task = models.TaskModel.objects.get(pk = id)
    taskk = forms.Tas_Form(instance=task)
    if request.method == 'POST':
        task = forms.Tas_Form(request.POST, instance=task)
        if task.is_valid():
            task.save()
            return redirect('seetask')
        
    return render(request, 'tas.html', {'tsk':taskk})



def delete(request, id):
    task = models.TaskModel.objects.get(pk = id)
    task.delete()
    return redirect('seetask')