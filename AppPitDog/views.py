from django.shortcuts import render, redirect
from .models import Produtos, Cardapio, TipoProduto
from .forms import ProdutoForm, CardapioForm, CategoriaForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Carrinho, ItemCarrinho, Cardapio, Pedido, ItemPedido
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'AppPitDog/index.html')

def product(request):
    product = Produtos.objects.order_by('name')

    context = {"product": product}

    return render (request, 'AppPitDog/product.html', context)


def tipoProduto(request):
    tipo = TipoProduto.objects.order_by('TypeName')

    context = {"tipo": tipo}
    return render (request, 'AppPitDog/tipoProduto.html', context)

def cardapio(request):
    # cardapio = Cardapio.objects.order_by('name')
    # tipoProduto = Produtos.objects.order_by('name')

    categorias = TipoProduto.objects.all()  
    cardapio = Cardapio.objects.order_by('name') 


    context = {"cardapio": cardapio, 'categorias': categorias}
    return render (request, 'AppPitDog/cardapio.html', context)

def cardapioDetalhes(request, cardapio_id):
    detalhe = Cardapio.objects.get(id = cardapio_id)
    ingredients = detalhe.ingredients.all()
    context = {'detalhe': detalhe, 'ingredientes': ingredients}

    return render(request, 'AppPitDog/detalhe.html', context)


# funções de criar

def novoProduto(request):
    if request.method != 'POST':
        form = ProdutoForm()
    else:
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product'))
        
    context = {'form': form}
    return render(request, 'AppPitDog/novo_produto.html',context)


def novoPrato(request):
    if request.method != 'POST':
        form = CardapioForm()
    else:
        form = CardapioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cardapio'))
    context = {'form': form}
    return render(request, 'AppPitDog/novo_prato.html',context)



def novaCategoria(request):
    if request.method != 'POST':
        form = CategoriaForm()
    else:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tipoProduto'))
    context = {'form': form}
    return render(request, 'AppPitDog/nova_categoria.html',context)


# funções de editar

def editProduto(request, product_id):
    produto = Produtos.objects.get(id = product_id)

    if request.method != 'POST':
        form = ProdutoForm(instance=produto)
    else:
        form = ProdutoForm(instance=produto, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('product'))
    
    context = {'produto': produto, 'form': form}
    return render(request, 'AppPitDog/edit_produto.html', context)



def editPrato(request, prato_id):
    prato = Cardapio.objects.get(id = prato_id)

    if request.method != 'POST':
        form = CardapioForm(instance=prato)
    else:
        form = CardapioForm(instance=prato, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cardapio'))
    
    context = {'prato': prato, 'form': form}
    return render(request, 'AppPitDog/edit_prato.html', context)


def editCategoria(request, categoria_id):
    categoria = TipoProduto.objects.get(id = categoria_id)

    if request.method != 'POST':
        form = CategoriaForm(instance=categoria)
    else:
        form = CategoriaForm(instance=categoria, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tipoProduto'))
    
    context = {'categoria': categoria, 'form': form}
    return render(request, 'AppPitDog/edit_categoria.html', context)

# funções de deletar.


def deleteProduto(request, produto_id):
    produto = Produtos.objects.get(id=produto_id)
    produto.delete()

    return HttpResponseRedirect(reverse('product'))

def deleteCardapio(request, prato_id):
    prato = Cardapio.objects.get(id=prato_id)
    prato.delete()

    return HttpResponseRedirect(reverse('cardapio'))


def deleteCategoria(request, categoria_id):
    categoria = TipoProduto.objects.get(id=categoria_id)
    categoria.delete()

    return HttpResponseRedirect(reverse('tipoProduto'))



# ***************************************************************************


def get_carrinho(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
    carrinho, created = Carrinho.objects.get_or_create(session_key=request.session.session_key)
    return carrinho


def adicionar_ao_carrinho(request, prato_id):
    carrinho = get_carrinho(request)
    prato = get_object_or_404(Cardapio, id=prato_id)

    item, created = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        prato=prato
    )
    if not created:
        item.quantidade += 1
    item.save()

    return redirect('cardapio')


def ver_carrinho(request):
    carrinho = get_carrinho(request)
    itens = carrinho.itens.all()

    total = sum(item.total_item() for item in itens)

    context = {'itens': itens, 'total': total}
    return render(request, 'AppPitDog/carrinho.html', context)


def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    else:
        item.delete()
    return redirect('ver_carrinho')

# ***************************************************************************


def finalizar_pedido(request):
    carrinho = get_carrinho(request)
    itens_carrinho = carrinho.itens.all()

    if not itens_carrinho:
        return redirect('ver_carrinho')
    
    pedido = Pedido.objects.create(session_key=request.session.session_key)
    
    for item in itens_carrinho:
        ItemPedido.objects.create(
            pedido=pedido,
            prato=item.prato,
            quantidade=item.quantidade
        )

    carrinho.itens.all().delete()

    return redirect('producao')


def producao(request):
    pedidos = Pedido.objects.all().order_by('-criado_em')
    context = {'pedidos': pedidos}  
    return render(request, 'AppPitDog/producao.html', context)


def atualizar_status(request, pedido_id, novo_status):
    pedido = Pedido.objects.get(id=pedido_id)
    pedido.status = novo_status
    pedido.save()
    return redirect('producao')
