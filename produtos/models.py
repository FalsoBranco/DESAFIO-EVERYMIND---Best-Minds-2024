import uuid

from django.db import models


    #  - Nome do produto
    #  - Código do produto
    #  - Descrição do produto
    #  - Preço do produto
# Create your models here.
class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField("Nome", max_length=100)
    descricao = models.TextField("Descrição", blank=True)
    preco = models.DecimalField("Preço", decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self):
        return self.nome

        return self.nome

