# Generated by Django 4.0.6 on 2022-08-25 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True, verbose_name='Categoria')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.CharField(max_length=10, verbose_name='Un')),
            ],
            options={
                'verbose_name': 'Unidade de Medida',
                'verbose_name_plural': 'Unidades de Medida',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('nome', models.CharField(max_length=255, unique=True, verbose_name='Produto')),
                ('ncm', models.CharField(blank=True, max_length=10, verbose_name='NCM')),
                ('cst', models.CharField(blank=True, max_length=3, verbose_name='CST')),
                ('cfop', models.CharField(blank=True, max_length=4, verbose_name='CFOP')),
                ('peso_barra', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Peso Barra')),
                ('icms_1', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='ICMS Interno 1')),
                ('icms_2', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='ICMS Interno 2')),
                ('ipi', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='IPI')),
                ('mva', models.CharField(blank=True, max_length=3, verbose_name='MVA')),
                ('imagem', models.ImageField(blank=True, upload_to='produtos/%Y', verbose_name='Imagem do produto')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor de Custo')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Preço')),
                ('disponivel', models.BooleanField(default=True, verbose_name='Disponível')),
                ('quant_produto', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Quantidade de Produto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedor.fornecedor')),
                ('unimed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.unidademedida', verbose_name='Unidade de medida')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['nome'],
            },
        ),
    ]
