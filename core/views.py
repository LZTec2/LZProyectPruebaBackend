# ...existing code...
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QR
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

# Create your views here.
