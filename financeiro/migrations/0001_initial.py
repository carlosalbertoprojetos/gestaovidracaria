# Generated by Django 4.1.1 on 2022-10-24 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedor', '0001_initial'),
        ('cliente', '0001_initial'),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código Compra')),
                ('data_compra', models.DateField(verbose_name='Data Compra')),
                ('formapgto', models.CharField(choices=[('Pix', 'pix'), ('Cartão', 'cartão'), ('Dinheiro', 'dinheiro')], max_length=11, verbose_name='Forma pgto')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='nfs_compras')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Custo da Compra R$')),
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
                ('data_venda', models.DateField(verbose_name='Data Venda')),
                ('formapgto', models.CharField(choices=[('Pix', 'pix'), ('Cartão', 'cartão'), ('Dinheiro', 'dinheiro')], max_length=11, verbose_name='Forma pgto')),
                ('custo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Custo da venda R$')),
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
                ('quantidade', models.PositiveSmallIntegerField(default=0, verbose_name='Quantidade')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Preço de Venda R$')),
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
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor')),
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
                ('quantidade', models.IntegerField(null=True, verbose_name='Quantidade')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Preço de Compra R$')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subtotal R$')),
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
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor')),
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
