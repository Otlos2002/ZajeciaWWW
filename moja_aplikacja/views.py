from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Osoba, Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer

# Osoba Endpoints

@api_view(['GET'])
def get_osoby(request):
    osoby = Osoba.objects.all()
    serializer = OsobaModelSerializer(osoby, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_osoba(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_osoba(request):
    serializer = OsobaModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_osoba(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def search_osoby(request, nazwa):
    osoby = Osoba.objects.filter(nazwisko__icontains=nazwa)  # Filtruj osoby według nazwiska
    serializer = OsobaModelSerializer(osoby, many=True)
    return Response(serializer.data)

# Stanowisko Endpoints

@api_view(['GET'])
def get_stanowiska(request):
    stanowiska = Stanowisko.objects.all()
    serializer = StanowiskoModelSerializer(stanowiska, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_stanowisko(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
        serializer = StanowiskoModelSerializer(stanowisko)
        return Response(serializer.data)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_stanowisko(request):
    serializer = StanowiskoModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_stanowisko(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
