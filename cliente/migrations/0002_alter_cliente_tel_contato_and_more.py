# Generated by Django 4.0.6 on 2022-09-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tel_contato',
            field=models.CharField(blank=True, max_length=11, unique=True, verbose_name='Telefone Contato'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tel_principal',
            field=models.CharField(blank=True, max_length=11, unique=True, verbose_name='Telefone Principal'),
        ),
    ]
