from django.db import models
# para importar os usuários do django
from django.contrib.auth.models import User

# Create your models here.
# models.Model é o parâmetro recebido pelo db


class Evento (models.Model):
    # o tipo do campo é charfield com no maximo 100 caracteres
    titulo = models.CharField(max_length=100)
    # permite q a descrição seja em branco ou nula
    descricao = models.TextField(blank=True, null=True)
    # data do evento n pode ser nula ou branco
    # vai aparecer esse nome ao invés da variavel
    data_evento = models.CharField(
        max_length=100, verbose_name='Data do Evento')
    # smp q for add um registro no bd, ele vai ser preeenchido automaticamente
    # (com a hr atual)
    data_criacao = models.DateTimeField(auto_now=True)
    # como vai ser multiusuário temos q criar uma chave estrangeira
    # cada usuário tem seus eventos
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # o segundo campo é qnd o usuário for deletado, deleta td (precisa preeencher esse campo p rodar)
# precisamos fazer essa classe virar uma tabela no bd migrando ela
# no terminal = python manage.py makemigrations core (migra só o core, se n ele migra td)
    # só o migrantions faz a migração direta no bd (esse comando acima n faz a migração propriamente dita)
    # ele cria em migrations um doc com o bd e cria um ID como primarykey
# python manage.py sqlmigrate core 0001 (faz o migate só dessa migração 0001)
    # cria e mostra no terminal a tabela no SQLight (ele cria o nome da tabela) (n faz o migrate propriamente dito)

    # define os metadados da tabela
    class Meta:
        db_table = 'evento'  # define o nome da tabela

    # para conf o título do objeto q eu criarei no banco com o título q eu escolhi usamos esse métodoS
    def __str__(self):
        return self.titulo  # pega o título q eu criei acima e coloca como título do obj

     # def get_data_evento(self):
        # é possivel criar funções no model p chamar no html
        # return self.data_evento.strftime('%d/%m/%Y')
