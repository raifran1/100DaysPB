from django.db import models
from django.utils import timezone

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.rua

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(default=timezone.now, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    STATUS_CHOICES = (
        ("A", "Aberto"),
        ("C", "Concluido")
    )
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='cliente')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.cliente.nome

class CarrinhoItem(models.Model):
    produto = models.ForeignKey("Produto", on_delete=models.CASCADE, related_name='produtoItem')
    carrinho = models.ForeignKey("Carrinho", on_delete=models.CASCADE, related_name='ItemCarrinho')
    valor = models.FloatField(null=False, blank=False)
    quantidade = models.IntegerField(blank=False, null=False)
    valorTotal = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.produto.nome

class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, related_name='clientePedido')
    observacoes = models.CharField(max_length=300, null=False, blank=False)
    data_pedido = models.DateTimeField(default=timezone.now, blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    carrinho = models.ForeignKey("Carrinho", on_delete=models.CASCADE, related_name='carrinhPedido')
    #produtos = models.ManyToManyField(Produto)
    #itens = models.ManyToManyField(CarrinhoItem)

    def __str__(self):
        return self.cliente.nome