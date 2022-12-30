from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=200)
    prioridad = models.IntegerField(default=1)
    creado_en = models.DateTimeField(auto_now_add=True)
    completado_en = models.DateTimeField(null=True)

    def __str__(self):
        return self.nombre

    def completar(self):
        self.completado_en = timezone.now()
        return self.save()
