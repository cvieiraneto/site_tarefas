from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefas, name='inicio'),
    path('helloworld/', views.helloworld, name='helloworld'),
    path('meunome/<str:nome>', views.printar_nome, name='meunome'),
    path('tarefa/<int:id>', views.mostrar_tarefa, name='task-view'),
    path('editar/<int:id>', views.editTask, name='task-edit'),
    path('deletar/<int:id>', views.deleteTask, name='delete-task'),
    path('adicionartarefa/', views.addTask, name='add-task'),
]