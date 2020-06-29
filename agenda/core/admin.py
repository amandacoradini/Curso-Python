from django.contrib import admin
from core.models import Evento  # importa a classe

# Register your models here.
# classe q define o q vai ser mostrado no admin


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario',)


# para registrar aquela classe criada no admin
# a classe evento registra a classe evento admin
admin.site.register(Evento, EventoAdmin)
