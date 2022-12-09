# Generated by Django 4.0.6 on 2022-11-01 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=200, verbose_name='Nome da Empresa')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('admissao', models.DateField(verbose_name='Data de Admissão')),
                ('cargo', models.CharField(blank=True, max_length=200, verbose_name='Cargo')),
                ('salario', models.CharField(blank=True, max_length=200, verbose_name='Salário')),
                ('nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('naturalidade', models.CharField(blank=True, max_length=200, verbose_name='Local de nascimento/UF')),
                ('vtransporte', models.TextField(blank=True, verbose_name='Vale Transporte')),
                ('residencial', models.CharField(blank=True, max_length=11, unique=True, verbose_name='Telefone Residencial')),
                ('celular', models.CharField(blank=True, max_length=11, unique=True, verbose_name='Celular')),
                ('escolaridade', models.CharField(blank=True, max_length=200, verbose_name='Escolaridade')),
                ('est_civil', models.CharField(blank=True, max_length=50, verbose_name='Estado Civil')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'M'), ('F', 'F'), ('OUTRO', 'OUTRO'), ('PREFIRO NÃO DIZER', 'PREFIRO NÃO DIZER')], max_length=18, verbose_name='Sexo')),
                ('raca', models.CharField(blank=True, choices=[('BRANCA', 'BRANCA'), ('PRETA', 'PRETA'), ('PARDA', 'PARDA'), ('AMARELA', 'AMARELA'), ('INDÍGENA', 'INDÍGENA')], max_length=8, verbose_name='Raça/Cor')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='E-mail')),
                ('rg', models.CharField(blank=True, max_length=7, verbose_name='RG')),
                ('data_rg', models.DateField(verbose_name='Data de Expedição')),
                ('cpf', models.CharField(blank=True, max_length=14, unique=True, verbose_name='CPF')),
                ('ctps', models.CharField(blank=True, max_length=50, verbose_name='CTPS/SÉRIE/UF')),
                ('pis', models.CharField(blank=True, max_length=15, verbose_name='PIS')),
                ('titulo', models.CharField(blank=True, max_length=200, verbose_name='TITULO/SEÇÃO/ZONA/UF')),
                ('cnh', models.CharField(blank=True, max_length=50, verbose_name='CNH')),
                ('logradouro', models.CharField(blank=True, max_length=200, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=30, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('cep', models.CharField(blank=True, max_length=11, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('pai', models.CharField(blank=True, max_length=200, verbose_name='Nome do Pai')),
                ('mae', models.CharField(blank=True, max_length=200, verbose_name='Nome da Mãe')),
                ('conjuge', models.CharField(blank=True, max_length=20, verbose_name='Nome do Cônjuge')),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='conta.conta', verbose_name='Banco')),
            ],
        ),
        migrations.CreateModel(
            name='Filho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=200, verbose_name='Nome do Filho')),
                ('data', models.DateField(verbose_name='Data de Nascimento')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='funcionario.funcionario', verbose_name='Funcionario')),
            ],
        ),
    ]
