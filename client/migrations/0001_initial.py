# Generated by Django 4.0.6 on 2023-01-19 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_contato', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('tel_principal', models.CharField(blank=True, max_length=11, verbose_name='Telefone Principal')),
                ('tel_contato', models.CharField(blank=True, max_length=11, verbose_name='Telefone Contato')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('cpf', models.CharField(blank=True, max_length=14, verbose_name='CPF')),
                ('cnpj', models.CharField(blank=True, max_length=18, verbose_name='CNPJ')),
                ('insc_estadual', models.CharField(blank=True, max_length=15, verbose_name='Inscrição Estadual')),
                ('logradouro', models.CharField(blank=True, max_length=200, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=30, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('cep', models.CharField(blank=True, max_length=11, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.CharField(max_length=200, verbose_name='Responsável da Obra')),
                ('logradouro', models.CharField(blank=True, max_length=200, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=30, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('cep', models.CharField(blank=True, max_length=11, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='client.client', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Obra',
            },
        ),
    ]