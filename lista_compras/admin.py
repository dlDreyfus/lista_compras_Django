# Importa o módulo admin, necessário para configurar o painel administrativo
from django.contrib import admin
# Importa a classe Item do arquivo models.py que está na mesma pasta
from .models import Item

# Register your models here.
# Registra o modelo Item no site administrativo para que ele apareça na interface
admin.site.register(Item)
