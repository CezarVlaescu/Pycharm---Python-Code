from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):

    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    dict = {'tasks': tasks, 'form': form}
    return render(request, 'app/list.html', dict)

def Update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task )
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'app/update_data.html', context)

def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    dict = {'item': item}
    return render(request, 'app/delete.html', dict)






