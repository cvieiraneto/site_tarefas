from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('helloworld/', views.helloworld, name='helloworld'),
    path('meunome/<str:nome>', views.printar_nome, name='meunome')
]