# Generated by Django 4.0.6 on 2023-01-19 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedor', '0001_initial'),
        ('produto', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código da Compra')),
                ('data', models.DateField(verbose_name='Data da Compra')),
                ('formapgto', models.CharField(choices=[('Boleto', 'Boleto'), ('Cheque', 'Cheque'), ('C/Entrega', 'C/Entrega'), ('Pix', 'Pix'), ('Cartão', 'Cartão'), ('Dinheiro', 'Dinheiro')], max_length=11, verbose_name='Forma de Pagamento')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='nfs_compras')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Total da Compra')),
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
                ('codigo', models.CharField(max_length=10, verbose_name='Código da Venda')),
                ('data', models.DateField(verbose_name='Data da Venda')),
                ('formapgto', models.CharField(choices=[('Boleto', 'Boleto'), ('Cheque', 'Cheque'), ('C/Entrega', 'C/Entrega'), ('Pix', 'Pix'), ('Cartão', 'Cartão'), ('Dinheiro', 'Dinheiro')], max_length=11, verbose_name='Forma de Pagamento')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Total da Venda')),
                ('status', models.CharField(choices=[('Pendente', 'pendente'), ('Aguardando', 'aguardando'), ('Entregue', 'entregue'), ('Cancelado', 'cancelado')], default='pendente', max_length=10, verbose_name='Condição')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.client')),
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
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=5, max_digits=10, null=True, verbose_name='Valor Produto')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subtotal')),
                ('detalhes', models.CharField(blank=True, max_length=300, verbose_name='Detalhes da Venda')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produto.produto', verbose_name='Produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.venda')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='VendaPrestacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prestacao', models.CharField(max_length=5, verbose_name='Parcela')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor da Parcela')),
                ('vencimento', models.DateField(verbose_name='Vencimento')),
                ('pagamento', models.DateField(verbose_name='Pagamento')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.venda')),
            ],
            options={
                'verbose_name': 'Prestação',
                'verbose_name_plural': 'Prestações',
            },
        ),
        migrations.CreateModel(
            name='CompraProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=5, max_digits=10, null=True, verbose_name='Preço do Produto')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subtotal')),
                ('detalhes', models.CharField(blank=True, max_length=300, verbose_name='Detalhes da Compra')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.compra')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produto.produto', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='CompraPrestacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prestacao', models.CharField(max_length=5, verbose_name='Parcela')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor da Parcela')),
                ('vencimento', models.DateField(verbose_name='Vencimento')),
                ('pagamento', models.DateField(verbose_name='Pagamento')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.compra')),
            ],
            options={
                'verbose_name': 'Prestação',
                'verbose_name_plural': 'Prestações',
            },
        ),
    ]
