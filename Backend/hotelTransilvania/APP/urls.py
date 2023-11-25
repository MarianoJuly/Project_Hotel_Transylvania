# urls.py
from django.urls import path
from .views import  respostaFuncionario, respostaHotel

urlpatterns = [
   
    #url da aplicação
    path('funcionario/', respostaFuncionario.as_view()),
    path('funcionario/<int:id>', respostaFuncionario.as_view()),
   
    path('hotel/', respostaHotel.as_view()),
    path('hotel/<int:id>', respostaHotel.as_view())
    # Adicione outras URLs conforme necessário
]
