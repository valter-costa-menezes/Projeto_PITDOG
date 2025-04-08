from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class TipoProduto(models.Model):
    """Tipos de produtos que serão cadastrados"""
    TypeName = models.CharField(max_length=50)


    def __str__(self):
        """Representação visual no painel admin"""
        return self.TypeName


class Produtos(models.Model):
    """Produto que tem no estoque"""
    name = models.CharField(max_length=150)
    balence = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Representação visual no painel admin"""
        return self.name
    

class Cardapio(models.Model):
    """Pratos prontos do cardápio"""
    name = models.CharField(max_length=150)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.ManyToManyField(Produtos)
    price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Representação visual no painel admin"""
        return f"{self.name}:   R$ {self.price}"
    



# ***************************************************************************************

class Carrinho(models.Model):
    session_key = models.CharField(max_length=40)  # identificador da sessão do usuário
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho {self.id} - {self.session_key}"


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    prato = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.prato.name}"

    def total_item(self):
        return self.quantidade * self.prato.price
    
# ***************************************************************************************

STATUS = [
    ('aguardando', 'Aguardando'),
    ('produzindo','Produzindo'),
    ('finalizado', 'Finalizado')
]

class Pedido(models.Model):
    session_key = models.CharField(max_length=40)
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS, default='aguardando')

    def __str__(self):
        return f"Pedido {self.id} - {self.status}"
    

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    prato = models.ForeignKey(Cardapio, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.prato.name} - {self.quantidade}"