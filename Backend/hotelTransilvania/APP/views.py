
#Uma funcionalidade settada por arquivo
from .funcionalidades.funcionarioFuncs import retornaFuncionario,salvaFuncionario,deletaFuncionario,atualizaFuncionario
from .funcionalidades.hotelFuncs import retornaHotel,salvaHotel,deletaHotel,atualizaHotel
from .funcionalidades.quartoFuncs import retornaQuarto,salvaQuarto,atualizaQuarto,deletaQuarto
from .funcionalidades.clienteFuncs import retornaCliente,salvaCliente,deletaCliente,atualizaCliente
from rest_framework.views import APIView

#Reserva não será declarado no crud, pois se trada de uma relação mais elaborada e precisa de um tratamento melhor que uma simples tabela.

# Lógica de loging -------//
# Classe existe uma variavél de loging para determinada pessoa
# -> quando feito o loging voce receberá uma string que terá funcionalidade de tolken
# -> sempre que feito uma nova requisição você deverá utilizar sua string para aplicação garantir que vc está logado
# -> ATENÇÃO: essa aplicação não é escalavel pois o loging é carrergado em memória principal, caso muitos acessos travara o servidor

#class logado():


class respostaHotel(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        return retornaHotel(id)
                
    def post(self, request, id = 0):       
        return salvaHotel(request.data)     
    
    def delete(self, request, id=0):
        return deletaHotel(id)
    
    def put(self,request, id = 0): 
        return atualizaHotel(id,request)
        
class respostaFuncionario(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        return retornaFuncionario(id)
                
    def post(self, request, id = 0):       
        return salvaFuncionario(request.data)     
    
    def delete(self, request, id=0):
        return deletaFuncionario(id)
    
    def put(self,request, id = 0): 
        return atualizaFuncionario(id,request)
    
class respostaQuarto(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        return retornaQuarto(id)
                
    def post(self, request, id = 0):       
        return salvaQuarto(request.data)     
    
    def delete(self, request, id = 0):
        return deletaQuarto(id)
    
    def put(self,request, id = 0): 
        return atualizaQuarto(id,request)
    
class respostaCliente(APIView):
    
    #no get nos adicionamos um valor default do id == 0 para que possamos arrumar as rotas
    def get(self, request, id=0):
        return retornaCliente(id)
                
    def post(self, request, id = 0):       
        return salvaCliente(request.data)     
    
    def delete(self, request, id = 0):
        return deletaCliente(id)    
    
    def put(self,request, id = 0): 
        return atualizaCliente(id,request)


