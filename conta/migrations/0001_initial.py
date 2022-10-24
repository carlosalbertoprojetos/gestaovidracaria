# Generated by Django 4.1.1 on 2022-10-24 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Banco')),
                ('agencia', models.CharField(max_length=30, verbose_name='Agência')),
                ('conta', models.CharField(max_length=30, verbose_name='Nome da Conta')),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Saldo')),
                ('pix', models.CharField(blank=True, max_length=30, verbose_name='Chave PIX')),
                ('tel_contato', models.CharField(blank=True, max_length=11, unique=True, verbose_name='Telefone Contato')),
                ('logradouro', models.CharField(blank=True, max_length=200, verbose_name='Logradouro')),
                ('numero', models.CharField(blank=True, max_length=5, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('cep', models.CharField(blank=True, max_length=11, verbose_name='CEP')),
                ('estado', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='Estado')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
            ],
        ),
    ]
