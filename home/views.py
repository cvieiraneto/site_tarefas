from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# def home(request):
#     return HttpResponse("Hello, World")

def home(request):
    return render(request, 'helloworld.html')

def helloworld(request):
    return render(request, 'helloworld.html')

def printar_nome(request, nome):
    return render(request, 'printarNome.html', {'nome': nome})
def tarefas(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'tarefas':tasks})

def mostrar_tarefa(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'mostar_tarefa.html', {'tarefa':task})

def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) #pausa o salvamento
            task.done = 'not started'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'addtask.html', {'form':form})