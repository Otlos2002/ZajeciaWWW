# Testowanie serializerów w Django REST Framework

Ten plik zawiera przykłady użycia serializerów `OsobaModelSerializer` oraz `StanowiskoModelSerializer` do serializacji i deserializacji obiektów modeli `Osoba` i `Stanowisko` w Django REST Framework.

### Wymagania wstępne

Aby przetestować poniższe przykłady, należy uruchomić Django shell:

```bash
python manage.py shell


#Importowanie serializatorów
from moja_aplikacja.models import Osoba, Stanowisko
from moja_aplikacja.serializers import OsobaModelSerializer, StanowiskoModelSerializer
# Serializacja obiektów modelu Osoba
# Zakładamy, że w bazie danych istnieje przynajmniej jedna instancja Osoba
osoba = Osoba.objects.first()
osoba_serializer = OsobaModelSerializer(osoba)

# Sprawdzanie zserializowanych danych
print(osoba_serializer.data)

#Deserializacja danych do utworzenia nowej instancji
new_osoba_data = {
    "imie": "Anna",
    "nazwisko": "Nowak",
    "plec": 2,
    "stanowisko": 1
}

osoba_serializer = OsobaModelSerializer(data=new_osoba_data)
if osoba_serializer.is_valid():
    new_osoba = osoba_serializer.save()
    print("Utworzono nową osobę:", new_osoba)
else:
    print("Błędy walidacji:", osoba_serializer.errors)

# Serializacja obiektów modelu Stanowisko
# Zakładamy, że w bazie danych istnieje przynajmniej jedna instancja Stanowisko
stanowisko = Stanowisko.objects.first()
stanowisko_serializer = StanowiskoModelSerializer(stanowisko)

# Sprawdzanie zserializowanych danych
print(stanowisko_serializer.data)

# Deserializacja danych do utworzenia nowej instancji Stanowisko

new_stanowisko_data = {
    "nazwa": "Inżynier",
    "opis": "Odpowiedzialny za projektowanie i rozwój"
}

stanowisko_serializer = StanowiskoModelSerializer(data=new_stanowisko_data)
if stanowisko_serializer.is_valid():
    new_stanowisko = stanowisko_serializer.save()
    print("Utworzono nowe stanowisko:", new_stanowisko)
else:
    print("Błędy walidacji:", stanowisko_serializer.errors)
