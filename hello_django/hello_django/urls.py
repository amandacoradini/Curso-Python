from django.contrib import admin
from django.urls import include, path
from core import views

# url é onde coloca a rota
urlpatterns = [
    # o caminho é o próprio endereço do host e o include
    # me leva ao método que vai imprimir alguma coisa na tela
    # o método é criado no views so APP
    # path("", include("hello.urls")),
    path("hello/", views.hello),
]
