from django.contrib import admin
from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from moja_aplikacja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #osoba endpoints
    path('osoby/', views.get_osoby, name='get_osoby'),
    path('osoby/<int:pk>/', views.get_osoba, name='get_osoba'),
    path('osoby/create/', views.create_osoba, name='create_osoba'),
    path('osoby/delete/<int:pk>/', views.delete_osoba, name='delete_osoba'),
    path('osoby/search/<str:nazwa>/', views.search_osoby, name='search_osoby'),
    #stanowisko endpoints
    path('stanowiska/', views.get_stanowiska, name='get_stanowiska'),
    path('stanowiska/<int:pk>/', views.get_stanowisko, name='get_stanowisko'),
    path('stanowiska/create/', views.create_stanowisko, name='create_stanowisko'),
    path('stanowiska/delete/<int:pk>/', views.delete_stanowisko, name='delete_stanowisko'),

] + debug_toolbar_urls()





