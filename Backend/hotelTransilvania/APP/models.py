# models.py
from django.db import models

class Cliente(models.Model):
    id =  models.AutoField(primary_key=True, auto_created=True, editable=False)
    nome = models.CharField(max_length=500, null=False)
    idade = models.PositiveIntegerField()
    
class Funcionario(models.Model):
    id =  models.AutoField(primary_key=True, auto_created=True, editable=False)
    nome = models.CharField(max_length=500, null=False)
    cpf = models.CharField(max_length=15, null=False)

class Hotel(models.Model):
    id =  models.AutoField(primary_key=True, auto_created=True, editable=False)
    nome = models.CharField(max_length=500, null=False)
    quantQuarto = models.PositiveIntegerField(default= 0)
    localizacao = models.CharField(max_length=500, null=False, default=0)

class Quarto(models.Model):
    numero = models.PositiveIntegerField(primary_key=True)
    camasSolteiro = models.PositiveIntegerField()
    camasCasal = models.PositiveIntegerField()
    idHotel = models.OneToOneField(Hotel, on_delete=models.PROTECT, null=False, default=0)

class Reserva(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    id_cliente = models.OneToOneField(Cliente, on_delete=models.PROTECT, null=False, default=0)
    id_quarto = models.OneToOneField(Quarto, on_delete=models.PROTECT, null=False)
    id_Hotel = models.OneToOneField(Hotel, on_delete=models.PROTECT, null=False) 
    dataEntrada = models.DateField(default=0)
    dataSaida = models.DateField(default=0)
    emAtividade = models.BooleanField(default=False)


    