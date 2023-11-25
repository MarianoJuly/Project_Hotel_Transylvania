from ..serializers import HotelSerializer
from ..models import Hotel
from rest_framework import status
from rest_framework.response import Response

def retornaHotel(id=0):
    if id != 0:    
        Hotels = Hotel.objects.filter(id = id)
        serializer = HotelSerializer(Hotels, many=True)
        return Response(serializer.data)
            
    elif id == 0: 
        Hotels = Hotel.objects.all()
        serializer = HotelSerializer(Hotels, many=True)
        return Response(serializer.data)

def salvaHotel(dataParam):
    serializer = HotelSerializer(data=dataParam)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deletaHotel():
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
    