from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Osoba, Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer

@api_view(['GET'])
def get_osoby(request):
    osoby = Osoba.objects.all()
    serializer = OsobaModelSerializer(osoby, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_osoba(request):
    serializer = OsobaModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_stanowiska(request):
    stanowiska = Stanowisko.objects.all()
    serializer = StanowiskoModelSerializer(stanowiska, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_stanowisko(request):
    serializer = StanowiskoModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
