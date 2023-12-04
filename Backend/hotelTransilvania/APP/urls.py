# urls.py
from django.urls import path
from .views import  respostaFuncionario, respostaHotel, respostaQuarto, respostaCliente

urlpatterns = [
   
    #url da aplicação
    path('cliente/', respostaCliente.as_view()),
    path('cliente/<int:id>', respostaCliente.as_view()),

    path('funcionario/', respostaFuncionario.as_view()),
    path('funcionario/<int:id>', respostaFuncionario.as_view()),
   
    path('hotel/', respostaHotel.as_view()),
    path('hotel/<int:id>', respostaHotel.as_view()),

    path('quarto/', respostaQuarto.as_view()),
    path('quarto/<int:id>', respostaQuarto.as_view())
    # Adicione outras URLs conforme necessário
]
