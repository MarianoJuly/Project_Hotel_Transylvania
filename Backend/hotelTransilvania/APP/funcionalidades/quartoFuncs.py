from ..serializers import QuartoSerializer
from ..models import Quarto
from rest_framework import status
from rest_framework.response import Response

def retornaQuarto(id=0):
    if id != 0:    
        Quartos = Quarto.objects.filter(id = id)
        serializer = QuartoSerializer(Quartos, many=True)
        return Response(serializer.data)
            
    elif id == 0: 
        Quartos = Quarto.objects.all()
        serializer = QuartoSerializer(Quartos, many=True)
        return Response(serializer.data)

def salvaQuarto(dataParam):
    serializer = QuartoSerializer(data=dataParam)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deletaQuarto(id):
    if id != 0:
        try:
            Quartos = Quarto.objects.get(numero=id)
            Quartos.delete()
            return Response("ok")
        except Quarto.DoesNotExist:
            return Response("not ok")
        
    else:
        Quartos = Quarto.objects.all()
        Quartos.delete()
        return Response("deletados") 
    
def atualizaQuarto(id, request):
    if id != 0:
        # Isso retorna um objeto único ou None
        quarto = Quarto.objects.filter(numero = id).first()

        if quarto:
            quarto.camasCasal = request.data.get('camasCasal', quarto.camasCasal)
            quarto.camasSolteiro = request.data.get('camasSolteiro', quarto.camasSolteiro)
            #return Response(quarto.camasSolteiro)
            #return Response(quarto.camasCasal)
            #return Response(request.data)
            serializer = QuartoSerializer(quarto, data=request.data, partial = True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        
        return Response("Quarto não encontrado ou dados inválidos", status=404)

    return Response("ID inválido", status=400) 

