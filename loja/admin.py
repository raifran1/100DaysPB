from django.contrib import admin
from .models import Endereco, Cliente, Produto, Pedido, CarrinhoItem, Carrinho

# Register your models here.
admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(CarrinhoItem)
admin.site.register(Carrinho)