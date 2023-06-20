from django.contrib import admin

#Importar as classes

from.models import Funcionario, Movimentacao

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Movimentacao)
