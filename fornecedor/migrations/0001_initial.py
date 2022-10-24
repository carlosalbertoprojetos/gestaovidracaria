# Generated by Django 4.1.1 on 2022-10-24 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoFornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Fornecedor')),
                ('contato', models.CharField(max_length=200, verbose_name='Nome do Contato')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='E-mail')),
                ('cnpj', models.CharField(blank=True, max_length=18, unique=True, verbose_name='CNPJ')),
                ('insc_estadual', models.CharField(blank=True, max_length=15, unique=True, verbose_name='Inscrição Estadual')),
                ('logradouro', models.CharField(blank=True, max_length=200, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=30, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('cep', models.CharField(blank=True, max_length=11, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='conta.conta', verbose_name='Banco')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['nome'],
            },
        ),
    ]
