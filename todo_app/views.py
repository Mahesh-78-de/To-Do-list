from django.shortcuts import redirect, render
from django.tasks import Task

    

def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        if task:
            Task.objects.create(task=task)
    return redirect('index')


# Create your views here.
