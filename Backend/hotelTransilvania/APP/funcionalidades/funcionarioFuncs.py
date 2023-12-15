from ..serializers import FuncionarioSerializer
from ..models import Funcionario
from rest_framework import status
from django.http import JsonResponse
from rest_framework.response import Response

#logging
class Logging:
    logado = False

    # Método estático para obter o valor do atributo logado
    @staticmethod
    def get_logado():
        return Logging.logado

    # Método estático para definir o atributo como True
    @staticmethod
    def logar():
        Logging.logado = True
        return "Logado"

    # Método estático para definir o atributo como False
    @staticmethod
    def deslogar():
        Logging.logado = False
        return "Deslogado"
    
def deslogar():
    Logging.deslogar()
    return Response(Logging.get_logado())



def logar(cpf=0, senha=0):
    if cpf != 0:
       
        funcionarios = Funcionario.objects.filter(cpf=cpf, senha=senha)
        
        if funcionarios.exists():
            Logging.logar()
            serializer = FuncionarioSerializer(funcionarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            
            return Response("Credenciais inválidas", status=status.HTTP_401_UNAUTHORIZED)
    else:
        print("credenciais invalidas")
        return Response("Campos inválidos", status=status.HTTP_400_BAD_REQUEST)
     

def retornaFuncionario(cpf=0):
      if cpf != 0:    
        Funcionarios = Funcionario.objects.filter(cpf = cpf)
        serializer = FuncionarioSerializer(Funcionarios, many=True)
        return Response(serializer.data)
            
      elif cpf == 0: 
        Funcionarios = Funcionario.objects.all()
        serializer = FuncionarioSerializer(Funcionarios, many=True)
        return Response(serializer.data)
      
def salvaFuncionario(dataParam):
    
    serializer = FuncionarioSerializer(data=dataParam)
    print(serializer)
    print(dataParam)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
def deletaFuncionario(cpf=0):
    if cpf != 0:
        try:
            print(cpf)
            Funcionarios = Funcionario.objects.get(cpf=cpf)
            Funcionarios.delete()
            return Response("ok")
        except Funcionario.DoesNotExist:
            return Response("not ok")
        
    else:
        Funcionarios = Funcionario.objects.all()
        Funcionarios.delete()
        return Response("deletados") 
    
def atualizaFuncionario(cpf, request):
    if cpf != 0:
        # Isso retorna um objeto único ou None
        funcionario = Funcionario.objects.filter(cpf=cpf).first()

        if funcionario:
            funcionario.nome = request.data.get('nome', funcionario.nome)
            serializer = FuncionarioSerializer(funcionario, data=request.data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response("Funcionario não encontrado ou dados inválidos", status=404)

    return Response("ID inválido", status=400)    



