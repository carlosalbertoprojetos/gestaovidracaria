# Generated by Django 4.0.6 on 2022-12-12 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operacao', models.CharField(choices=[('Compra', 'compra'), ('Venda', 'venda'), ('Outros', 'outros')], max_length=6, verbose_name='Operação')),
                ('data', models.DateField(verbose_name='Data')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Total de Produtos')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Valor Total do Movimento')),
                ('status', models.CharField(choices=[('Pendente', 'pendente'), ('Aguardando', 'aguardando'), ('Entregue', 'entregue'), ('Cancelado', 'cancelado')], default='pendente', max_length=10, verbose_name='Condição')),
                ('local', models.CharField(max_length=255, verbose_name='Local')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='funcionario.funcionario')),
            ],
            options={
                'verbose_name': 'Movimentação de Estoque',
                'verbose_name_plural': 'Movimentação de Estoque',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProdutoMovimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('preco', models.DecimalField(decimal_places=2, default=5, max_digits=10, verbose_name='Preço')),
                ('detalhes', models.CharField(blank=True, max_length=300, verbose_name='Detalhes')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subtotal')),
                ('movimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimento.movimento')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produto.produto', verbose_name='Produto')),
            ],
        ),
    ]
