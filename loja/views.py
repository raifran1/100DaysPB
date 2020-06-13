from django.shortcuts import render
from .models import CarrinhoItem, Pedido, Produto, Carrinho

def listar_produtos(request, id):
	pedido = Pedido.objects.filter(pk=id)


	dados = {
		'pedido': pedido
	}
	return render(request, 'produtos.html')