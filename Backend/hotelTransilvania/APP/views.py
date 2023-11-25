from django.shortcuts import render
from rest_framework import generics
from .models import Funcionario, Hotel
from .funcionalidades.funcionarioFuncs import retornaFuncionario,salvaFuncionario,deletaFuncionario
from .funcionalidades.hotelFuncs import retornaHotel,salvaHotel,deletaHotel
from .serializers import FuncionarioSerializer, ClienteSerializer, QuartoSerializer, ReservaSerializer, HotelSerializer
from rest_framework.views import APIView



class respostaHotel(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        return retornaHotel(id)
                
    def post(self, request, id = 0):       
        return salvaHotel(request.data)     
    
    def delete(self, request, id=0):
        return deletaHotel(id)


class respostaFuncionario(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        return retornaFuncionario(id)
                
    def post(self, request, id = 0):       
        return salvaFuncionario(request.data)     
    
    def delete(self, request, id=0):
        return deletaFuncionario(id)
    


    