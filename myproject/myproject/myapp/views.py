from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm 

# Create your views here.
def task_list(request):
    tasks = Task.objects.all() 

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})

    

