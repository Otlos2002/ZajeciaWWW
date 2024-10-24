from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Osoba
from .serializers import OsobaSerializer

@api_view(['GET'])
def get_osoby(request):
    osoby = Osoba.objects.all()
    serializer = OsobaSerializer(osoby, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_osoba(request):
    serializer = OsobaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

