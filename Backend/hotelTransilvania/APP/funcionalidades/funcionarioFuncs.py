from ..serializers import FuncionarioSerializer
from ..models import Funcionario
from rest_framework import status
from rest_framework.response import Response


def fazReserva(objetoReserva):
    return True

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
    
    if(dataParam.get('senha')):
        serializer = FuncionarioSerializer(data=dataParam)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response("Erro ao salvar funcionario", status=status.HTTP_400_BAD_REQUEST)

def deletaFuncionario(id):
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
    
def atualizaFuncionario(id, request):
    if id != 0:
        # Isso retorna um objeto único ou None
        funcionario = Funcionario.objects.filter(id=id).first()

        if funcionario:
            funcionario.nome = request.data.get('nome', funcionario.nome)
            serializer = FuncionarioSerializer(funcionario, data=request.data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response("Funcionario não encontrado ou dados inválidos", status=404)

    return Response("ID inválido", status=400)    

