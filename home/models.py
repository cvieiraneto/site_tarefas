from django.db import models

# Create your models here.

class Task(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    STATUS = (('not started', 'Não iniciado'), ('doing', 'Fazendo'), ('Done', 'Finalizado'))
    done = models.CharField(max_length=11, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo