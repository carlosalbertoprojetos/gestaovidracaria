# Generated by Django 4.0.6 on 2022-08-26 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0002_historico_alter_fornecedor_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Historico',
            new_name='HistoricoFornecedor',
        ),
    ]
