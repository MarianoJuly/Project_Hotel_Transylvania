# models.py
from django.db import models


class Funcionario(models.Model):
    
    cpf = models.CharField(primary_key=True, max_length=11)
    nome = models.CharField(max_length=200, null=False)
    senha = models.CharField(max_length=200, null=False)


class Cliente(models.Model):
    id =  models.AutoField(primary_key=True, auto_created=True, editable=False)
    nome = models.CharField(max_length=500, null=False)
    idade = models.PositiveIntegerField()


class Hotel(models.Model):
    id =  models.AutoField(primary_key=True, auto_created=True, editable=False)
    nome = models.CharField(max_length=500, null=False)
    quantQuarto = models.PositiveIntegerField(default= 0)
    temQuarto = models.BooleanField(default=False)
    localizacao = models.CharField(max_length=500, null=False, default=0)

    def __init__(self, nome, quantQuarto=0, temQuarto=False, localizacao='', *args, **kwargs):
        super(Hotel, self).__init__(*args, **kwargs)
        self.nome = nome
        self.quantQuarto = quantQuarto
        self.temQuarto = temQuarto
        self.localizacao = localizacao

    def aumentar_quantidade_quartos(self):
        self.quantQuarto += 1
        self.save()

        
class Quarto(models.Model):
    numero = models.PositiveIntegerField(primary_key=True)
    camasSolteiro = models.PositiveIntegerField()
    ocupado = models.BooleanField(default=False)
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

   