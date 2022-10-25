# Generated by Django 4.1.1 on 2022-10-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='valor_frete',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, verbose_name='valor para calculo do frete R$'),
        ),
    ]
