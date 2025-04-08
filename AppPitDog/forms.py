from django import forms
from .models import Produtos, Cardapio, TipoProduto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['name', 'balence']
        labels = {'name': 'Nome:', 'balence': 'Estoque inicial' }

class CardapioForm(forms.ModelForm):
    class Meta: 
        model = Cardapio
        fields = ['name', 'ingredients', 'price', 'tipo']
        labels = {'name': 'Nome do prato', 'ingredients': 'Produtos', 'price': 'Preço', 'tipo': 'tipo:'}


class CategoriaForm(forms.ModelForm):
    class Meta: 
        model = TipoProduto
        fields = ['TypeName']
        labels = {'TypeName': 'Nome da categoria'}