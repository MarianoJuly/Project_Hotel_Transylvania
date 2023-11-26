from ..serializers import ReservaSerializer
from ..models import Reserva
from rest_framework import status
from rest_framework.response import Response

def retornaReserva(id=0):
    if id != 0:    
        Reservas = Reserva.objects.filter(id = id)
        serializer = ReservaSerializer(Reservas, many=True)
        return Response(serializer.data)
            
    elif id == 0: 
        Reservas = Reserva.objects.all()
        serializer = ReservaSerializer(Reservas, many=True)
        return Response(serializer.data)

def salvaReserva(dataParam):
    serializer = ReservaSerializer(data=dataParam)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def deletaReserva(id):
    if id != 0:
        try:
            Reservas = Reserva.objects.get(id=id)
            Reservas.delete()
            return Response("ok")
        except Reserva.DoesNotExist:
            return Response("not ok")
        
    else:
        Reservas = Reserva.objects.all()
        Reservas.delete()
        return Response("deletados") 

def atualizaReserva(id, request):
    if id != 0:
        # Isso retorna um objeto único ou None
        reserva = Reserva.objects.filter(id=id).first()

        if reserva:
            reserva.data = request.data.get('nome', reserva.nome)
            serializer = ReservaSerializer(reserva, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response("Reserva não encontrada ou dados inválidos", status=404)

    return Response("ID inválido", status=400)  
