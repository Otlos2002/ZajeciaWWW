from rest_framework import serializers
from .models import Osoba, Stanowisko

# class OsobaSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     imie = serializers.CharField(max_length=100)
#     nazwisko = serializers.CharField(max_length=100)
#     plec = serializers.ChoiceField(choices=Osoba.Plec.choices)
#     stanowisko = serializers.CharField(source='stanowisko.nazwa', read_only=True)
#     data_dodania = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Osoba.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.imie = validated_data.get('imie', instance.imie)
#         instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
#         instance.plec = validated_data.get('plec', instance.plec)
#         instance.save()
#         return instance


class OsobaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']

class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']