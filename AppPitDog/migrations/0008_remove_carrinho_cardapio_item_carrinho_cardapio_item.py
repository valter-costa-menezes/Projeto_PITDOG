# Generated by Django 5.1.7 on 2025-03-31 03:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPitDog', '0007_remove_carrinho_cardapio_item_carrinho_cardapio_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='cardapio_item',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='cardapio_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AppPitDog.cardapio'),
        ),
    ]
