# Generated by Django 5.1.7 on 2025-03-31 03:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPitDog', '0008_remove_carrinho_cardapio_item_carrinho_cardapio_item'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrinho',
            old_name='data_pedido',
            new_name='criado_em',
        ),
        migrations.RemoveField(
            model_name='carrinho',
            name='cardapio_item',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('cardapio_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPitDog.cardapio')),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPitDog.carrinho')),
            ],
        ),
        migrations.AddField(
            model_name='carrinho',
            name='itens',
            field=models.ManyToManyField(through='AppPitDog.ItemCarrinho', to='AppPitDog.cardapio'),
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('cardapio_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPitDog.cardapio')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Aguardando', 'Aguardando'), ('Em produção', 'Em produção'), ('Preparado', 'Preparado')], default='Aguardando', max_length=20)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('itens', models.ManyToManyField(through='AppPitDog.ItemPedido', to='AppPitDog.cardapio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPitDog.pedido'),
        ),
    ]
