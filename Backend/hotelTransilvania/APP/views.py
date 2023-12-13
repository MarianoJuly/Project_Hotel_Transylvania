
#Uma funcionalidade settada por arquivo
from rest_framework.response import Response
from .funcionalidades.funcionarioFuncs import retornaFuncionario,salvaFuncionario,deletaFuncionario,atualizaFuncionario,logar,deslogar
from .funcionalidades.hotelFuncs import retornaHotel,salvaHotel,deletaHotel,atualizaHotel
from .funcionalidades.quartoFuncs import retornaQuarto,salvaQuarto,atualizaQuarto,deletaQuarto
from .funcionalidades.clienteFuncs import retornaCliente,salvaCliente,deletaCliente,atualizaCliente
from .funcionalidades.reservaFuncs import retornaReserva,salvaReserva,deletaReserva,atualizaReserva
from rest_framework.views import APIView
from .funcionalidades.funcionarioFuncs import Logging
#Reserva não será declarado no crud, pois se trada de uma relação mais elaborada e precisa de um tratamento melhor que uma simples tabela.

# Lógica de loging -------//
# Classe existe uma variavél de loging para determinada pessoa
# -> quando feito o loging voce receberá uma string que terá funcionalidade de tolken
# -> sempre que feito uma nova requisição você deverá utilizar sua string para aplicação garantir que vc está logado
# -> ATENÇÃO: essa aplicação não é escalavel pois o loging é carrergado em memória principal, caso muitos acessos travara o servidor

class respostaHotel(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return retornaHotel(id)
                
    def post(self, request, id = 0): 
        if(Logging.get_logado() == False):
            return Response("Faça logging")      
        return salvaHotel(request.data)     
    
    def delete(self, request, id=0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return deletaHotel(id)
    
    def put(self,request, id = 0): 
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return atualizaHotel(id,request)
        
class respostaFuncionario(APIView):

    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, cpf=0):
        return retornaFuncionario(cpf)  

    def post(self, request, cpf = 0):
              
        return salvaFuncionario(request.data)     
    
    def delete(self, cpf=0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return deletaFuncionario(cpf)
    
    def put(self,request, cpf = 0):
        if(Logging.get_logado() == False):
            return Response("Faça logging") 
        return atualizaFuncionario(cpf,request)
    
class respostaQuarto(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return retornaQuarto(id)
                
    def post(self, request, id = 0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")       
        return salvaQuarto(request.data)     
    
    def delete(self, request, id = 0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return deletaQuarto(id)
    
    def put(self,request, id = 0):
        if(Logging.get_logado() == False):
            return Response("Faça logging") 
        return atualizaQuarto(id,request)
    
class respostaCliente(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return retornaCliente(id)
                
    def post(self, request, id = 0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")       
        return salvaCliente(request.data)     
    
    def delete(self, request, id = 0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return deletaCliente(id)    
    
    def put(self,request, id = 0): 
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return atualizaCliente(id,request)

class respostaReserva(APIView):
     
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return retornaReserva(id)
                
    def post(self, request, id = 0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")       
        return salvaReserva(request.data)     
    
    def delete(self, request, id = 0):
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return deletaReserva(id)    
    
    def put(self,request, id = 0): 
        if(Logging.get_logado() == False):
            return Response("Faça logging")
        return atualizaReserva(id,request)

class Acessar(APIView):
    def get(self,request):
        if (deslogar() == False):
            return "deslogado"
        else: 
            return Response("Erro")
        
    def post(self, request):       
        return logar(request.data.get('cpf'), request.data.get('senha'))  
    

    