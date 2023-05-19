from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    