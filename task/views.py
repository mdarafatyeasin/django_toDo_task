from django.shortcuts import render, redirect
from . import forms
from . models import Task

# Create your views here.
def add_task(request):
    if request.method == "POST":
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid:
            task_form.save()
            return redirect('home_page')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form':task_form})

# edit task
def edit_task(request,id):
    task = Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    print(task.taskTitle)
    if request.method == "POST":
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid:
            task_form.save()
            return redirect('home_page')
    return render(request, 'add_task.html', {'form':task_form})

# delete task
def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home_page')