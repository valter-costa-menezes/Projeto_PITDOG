from django.contrib import admin
from AppPitDog.models import Produtos
from AppPitDog.models import TipoProduto
from AppPitDog.models import Cardapio
from AppPitDog.models import Pedido
from AppPitDog.models import ItemCarrinho
from AppPitDog.models import ItemPedido


admin.site.register(Produtos)
admin.site.register(TipoProduto)
admin.site.register(Cardapio)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(ItemCarrinho)



# Register your models here.
