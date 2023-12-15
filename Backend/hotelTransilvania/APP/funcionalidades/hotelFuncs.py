from ..serializers import HotelSerializer
from ..models import Hotel
from rest_framework import status
from rest_framework.response import Response

def temQuarto(id = id):
    if id != 0:    
        Hotels = Hotel.objects.first(id = id)
        return Hotels.temQuarto
    return "Hotel inexistente"    
    
def retornaHotel(id=0):
    if id != 0:    
        Hotels = Hotel.objects.filter(id = id)
        serializer = HotelSerializer(Hotels, many=True)
        return Response(serializer.data)
            
    elif id == 0: 
        Hotels = Hotel.objects.all()
        serializer = HotelSerializer(Hotels, many=True)
        return Response(serializer.data)

def adicionaQuarto(id, dataParam):
    if id != 0:
            # Isso retorna um objeto único ou None
            hotel = Hotel.objects.filter(id=id).first()

            if hotel:
                hotel.aumentar_quantidade_quartos()
                serializer = HotelSerializer(hotel, data=dataParam, partial=True)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
            
            return Response("Hotel não encontrado ou dados inválidos", status=404)

       

def salvaHotel(dataParam):
    # Crie uma instância do Hotel usando os dados fornecidos
    hotel = Hotel(nome=dataParam.get('nome'), quantQuarto=0, temQuarto=False, localizacao=dataParam.get('localizacao'))

    # Crie uma instância do serializer e passe a instância do Hotel
    serializer = HotelSerializer(instance=hotel, data=dataParam)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def deletaHotel(id):
    if id != 0:
        try:
            Hotels = Hotel.objects.get(id=id)
            Hotels.delete()
            return Response("ok")
        except Hotel.DoesNotExist:
            return Response("not ok")
        
    else:
        Hotels = Hotel.objects.all()
        Hotels.delete()
        return Response("deletados") 
    
def atualizaHotel(id, request):
    if id != 0:
        # Isso retorna um objeto único ou None
        hotel = Hotel.objects.filter(id=id).first()

        if hotel:
            hotel.nome = request.data.get('nome', hotel.nome)
            serializer = HotelSerializer(hotel, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response("Hotel não encontrado ou dados inválidos", status=404)

    return Response("ID inválido", status=400)