# Generated by Django 3.0.7 on 2020-06-06 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinhoitem',
            name='carrinho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ItemCarrinho', to='loja.Carrinho'),
        ),
        migrations.AlterField(
            model_name='carrinhoitem',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtoItem', to='loja.Produto'),
        ),
    ]