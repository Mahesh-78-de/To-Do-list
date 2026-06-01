from django.shortcuts import render, redirect, get_object_or_404
from todo_app.models import Task


def index(request):
    tasks = Task.objects.order_by('-created_at')
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def add_task(request):
    if request.method == 'POST':
        name = request.POST.get('task_name', '').strip()
        if name:
            Task.objects.create(task=name)
    return redirect('index')


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('index')