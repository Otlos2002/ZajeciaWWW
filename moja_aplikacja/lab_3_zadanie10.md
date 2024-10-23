# Zapytania do modelu Osoba w Django

1. Wyświetl wszystkie obiekty modelu Osoba
```python
wszystkie_osoby = Osoba.objects.all()
print("Wszystkie obiekty modelu Osoba:")
for osoba in wszystkie_osoby:
    print(osoba)

```
2. Wyświetl obiekt modelu Osoba z id = 3
```python
osoba_id_3 = Osoba.objects.get(id=3)
print("\nObiekt modelu Osoba z id = 3:")
print(osoba_id_3)
```

3. Wyświetl obiekty modelu Osoba, których imię rozpoczyna się na literę 'A'
```python
osoby_imie_A = Osoba.objects.filter(imie__startswith='A')
print("\nObiekty modelu Osoba, których imię zaczyna się na 'A':")
for osoba in osoby_imie_A:
    print(osoba)

```

4. Wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba
```python
unikalne_stanowiska = Osoba.objects.values_list('stanowisko', flat=True).distinct()
print("\nUnikalna lista stanowisk przypisanych dla modeli Osoba:")
for stanowisko_id in unikalne_stanowiska:
    stanowisko = Stanowisko.objects.get(id=stanowisko_id)
    print(stanowisko.nazwa)

```

5. Wyświetl nazwy stanowisk posortowane alfabetycznie malejąco
```python
stanowiska_posortowane = Stanowisko.objects.all().order_by('-nazwa')
print("\nNazwy stanowisk posortowane alfabetycznie malejąco:")
for stanowisko in stanowiska_posortowane:
    print(stanowisko.nazwa)
```

6. Dodaj nową instancję obiektu klasy Osoba i zapisz w bazie
```python
nowa_osoba = Osoba(imie='Jan', nazwisko='Kowalski', plec=Osoba.Plec.MEZCZYZNA, stanowisko=stanowiska_posortowane.first())
nowa_osoba.save()
print("\nDodano nową instancję obiektu klasy Osoba:")
print(nowa_osoba)
```

