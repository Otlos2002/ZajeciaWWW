from django.contrib import admin
from .models import Osoba, Stanowisko


class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'opis')
    search_fields = ('nazwa',)

class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania')
    readonly_fields = ('data_dodania',)
    search_fields = ('imie', 'nazwisko')
    list_filter = ('plec', 'stanowisko')
    date_hierarchy = 'data_dodania'

    @admin.display(description='Stanowisko (id)')
    def stanowisko_display(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)