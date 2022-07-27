# Generated by Django 4.0.6 on 2022-07-25 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0002_remove_cliente_num_venda'),
        ('produto', '0002_alter_produto_unimed'),
        ('fornecedor', '0002_alter_fornecedor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('formapgto', models.CharField(choices=[('Pix', 'pix'), ('Cartão', 'cartão'), ('Dinheiro', 'dinheiro')], max_length=11, verbose_name='Forma pgto')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='nfs_compras')),
                ('status', models.CharField(choices=[('Pendente', 'pendente'), ('Aguardando', 'aguardando'), ('Entregue', 'entregue'), ('Cancelado', 'cancelado')], default='pendente', max_length=10, verbose_name='Condição')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='fornecedor.fornecedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('num_venda', models.IntegerField(verbose_name='Nº Venda')),
                ('formapgto', models.CharField(choices=[('Pix', 'pix'), ('Cartão', 'cartão'), ('Dinheiro', 'dinheiro')], max_length=11, verbose_name='Forma pgto')),
                ('custo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Custo da venda')),
                ('status', models.CharField(choices=[('Pendente', 'pendente'), ('Aguardando', 'aguardando'), ('Entregue', 'entregue'), ('Cancelado', 'cancelado')], default='pendente', max_length=10, verbose_name='Condição')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cliente')),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
            },
        ),
        migrations.CreateModel(
            name='VendaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(null=True, verbose_name='Quantidade')),
                ('preço', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('detalhes', models.CharField(blank=True, max_length=300, verbose_name='Detalhes')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subtotal')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produto.produto', verbose_name='Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.venda')),
            ],
        ),
        migrations.CreateModel(
            name='CompraProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(null=True, verbose_name='Quantidade')),
                ('preço', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('detalhes', models.CharField(blank=True, max_length=300, verbose_name='Detalhes')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subtotal')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produto.produto', verbose_name='Produto')),
            ],
        ),
    ]