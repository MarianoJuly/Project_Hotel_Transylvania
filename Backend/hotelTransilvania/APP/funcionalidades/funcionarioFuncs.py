from ..serializers import FuncionarioSerializer
from ..models import Funcionario
from rest_framework import status
from rest_framework.response import Response

def retornaFuncionario(id=0):
    if id != 0:    
        Funcionarios = Funcionario.objects.filter(id = id)
        serializer = FuncionarioSerializer(Funcionarios, many=True)
        return Response(serializer.data)
            
    elif id == 0: 
        Funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(Funcionarios, many=True)
        return Response(serializer.data)

def salvaFuncionario(dataParam):
    serializer = FuncionarioSerializer(data=dataParam)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deletaFuncionario():
    if id != 0:
        try:
            Funcionarios = Funcionario.objects.get(id=id)
            Funcionarios.delete()
            return Response("ok")
        except Funcionario.DoesNotExist:
            return Response("not ok")
        
    else:
        Funcionarios = Funcionario.objects.all()
        Funcionarios.delete()
        return Response("deletados") 
    