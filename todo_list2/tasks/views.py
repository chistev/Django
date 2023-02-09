from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import *
from . import forms


def index(request):
    tasks = Task.objects.all()
    form = forms.TaskForm()

    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/index.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'tasks/delete_task.html', context)
