# Generated by Django 4.0.6 on 2022-10-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_rename_disponivel_produto_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='taxa_frete',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='valor_custo',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='valor_frete',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='valor_venda',
        ),
        migrations.AddField(
            model_name='produto',
            name='custo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Valor de Custo'),
        ),
        migrations.AddField(
            model_name='produto',
            name='frete',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, verbose_name='Valor do frete'),
        ),
        migrations.AddField(
            model_name='produto',
            name='venda',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Valor de Venda'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='aliquota_1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, verbose_name='Aliquota Interna 1'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='aliquota_2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=3, verbose_name='Aliquota Interna 2'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='peso_barra',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, verbose_name='Peso da Barra'),
        ),
    ]
