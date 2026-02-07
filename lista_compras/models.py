from django.db import models
from django.contrib.auth.models import User

# Define um modelo chamado Item, que será uma tabela no banco de dados
class Item(models.Model):
    # Linkamos o item a um usuário específico
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # Coluna para texto curto (até 100 letras), usada para o nome do produto
    nome = models.CharField(max_length=100)
    # Coluna para números inteiros, com valor padrão 1 se não for informado
    quantidade = models.IntegerField(default=1)
    # Coluna de Verdadeiro/Falso (checkbox), começa como Falso (não comprado)
    comprado = models.BooleanField(default=False)
    # Coluna de data/hora, preenchida automaticamente quando o item é criado
    criado_em = models.DateTimeField(auto_now_add=True)

    # Função que define como o item aparece escrito (ex: no painel admin)
    def __str__(self):
        return self.nome
