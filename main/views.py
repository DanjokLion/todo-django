from django.shortcuts import render, redirect
from .models import task
from .forms import taskForm

def index(request):
    tasks = task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    form = taskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


