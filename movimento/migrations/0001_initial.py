# Generated by Django 4.0.6 on 2022-08-09 03:44

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
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Total')),
                ('status', models.CharField(choices=[('Pendente', 'pendente'), ('Aguardando', 'aguardando'), ('Entregue', 'entregue'), ('Cancelado', 'cancelado')], default='pendente', max_length=10, verbose_name='Condição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='funcionario.funcionario')),
            ],
            options={
                'verbose_name': 'Movimento',
                'verbose_name_plural': 'Movimento',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProdutoMovimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(null=True, verbose_name='Quantidade')),
                ('preço', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('detalhes', models.CharField(blank=True, max_length=300, verbose_name='Detalhes')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subtotal')),
                ('movimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimento.movimento')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produto.produto', verbose_name='Produto')),
            ],
        ),
    ]
