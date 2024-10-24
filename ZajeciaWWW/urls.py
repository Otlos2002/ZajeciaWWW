from django.contrib import admin
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from moja_aplikacja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('osoby/', views.get_osoby, name='get_osoby'),
    path('osoby/create/', views.create_osoba, name='create_osoba'),
    path('stanowiska/', views.get_stanowiska, name='get_stanowiska'),
    path('stanowiska/create/', views.create_stanowisko, name='create_stanowisko'),
] + debug_toolbar_urls()





