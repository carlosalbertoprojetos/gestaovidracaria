# Generated by Django 4.0.6 on 2022-10-25 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0004_remove_compra_data_compra_compra_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compraproduto',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, default=5, max_digits=10, null=True, verbose_name='Preço do Produto'),
        ),
    ]
