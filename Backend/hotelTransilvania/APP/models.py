# models.py
from django.db import models

class Cliente(models.Model):
    id =  models.AutoField(primary_key=True, auto_created=True, editable=False)
    nome = models.CharField(max_length=500, null=False)
    idade = models.PositiveIntegerField()
    
class Funcionario(models.Model):
    id =  models.AutoField(primary_key=True, auto_created=True, editable=False)
    nome = models.CharField(max_length=500, null=False)

class Hotel(models.Model):
    id =  models.AutoField(primary_key=True, auto_created=True, editable=False)
    nome = models.CharField(max_length=500, null=False)

class Quarto(models.Model):
    numero = models.PositiveIntegerField(primary_key=True)
    camasSolteiro = models.PositiveIntegerField()
    camasCasal = models.PositiveIntegerField()

class Reserva(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    data = models.DateField(auto_now_add=True)


    