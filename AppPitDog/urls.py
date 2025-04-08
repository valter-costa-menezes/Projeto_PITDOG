
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('product', views.product, name='product'),
    path('cardapio', views.cardapio, name='cardapio'),
    path('tipoProduto', views.tipoProduto, name='tipoProduto'),
    path('cardapio/<cardapio_id>/', views.cardapioDetalhes, name='detalhe'),
    path('novoProduto', views.novoProduto, name='novo_produto'),
    path('novoPrato', views.novoPrato, name='novo_prato'),
    path('novaCategoria', views.novaCategoria, name='novo_categoria'),
    path('edit_produto/<int:product_id>/', views.editProduto, name='edit_produto'),
    path('edit_prato/<int:prato_id>/', views.editPrato, name='edit_prato'),
    path('edit_categoria/<int:categoria_id>/', views.editCategoria, name='edit_categoria'),
    path('deleteProduto/<int:produto_id>/', views.deleteProduto, name='delete_produto'),
    path('deletePrato/<int:prato_id>/', views.deleteCardapio, name='delete_prato'),
    path('deleteCategoria/<int:categoria_id>/', views.deleteCategoria, name='delete_categoria'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:prato_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),
    path('producao/', views.producao, name='producao'),
    path('atualizar_status/<int:pedido_id>/<str:novo_status>/', views.atualizar_status, name='atualizar_status'),


]
