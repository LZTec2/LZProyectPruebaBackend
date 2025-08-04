# ...existing code...
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QR
from django.db.models import Q
from rest_framework import serializers

# Serializer para QR
class QRSerializer(serializers.ModelSerializer):
    class Meta:
        model = QR
        fields = '__all__'


# API para crear QR (POST) y listar todos los QR (GET)
@api_view(['GET', 'POST'])
def qr_list_create(request):
    if request.method == 'GET':
        qrs = QR.objects.all()
        serializer = QRSerializer(qrs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener solo los QR públicos
@api_view(['GET'])
def qr_list_public(request):
    qrs = QR.objects.filter(isPublic=True)
    serializer = QRSerializer(qrs, many=True)
    return Response(serializer.data)

# Buscar un QR por su contenido exacto
@api_view(['GET'])
def qr_find_by_content(request, content):
    try:
        qr = QR.objects.get(content=content)
        serializer = QRSerializer(qr)
        return Response(serializer.data)
    except QR.DoesNotExist:
        return Response({'detail': 'QR not found'}, status=status.HTTP_404_NOT_FOUND)

# Buscar QR por texto (nombre, autor o contenido) en los públicos
@api_view(['GET'])
def qr_list_search(request):
    query = request.GET.get('q', '')
    qrs = QR.objects.filter(isPublic=True).filter(
        Q(name__icontains=query) |
        Q(author__icontains=query) |
        Q(content__icontains=query)
    )
    serializer = QRSerializer(qrs, many=True)
    return Response(serializer.data)

# Create your views here.
