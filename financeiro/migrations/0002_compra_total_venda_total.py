# Generated by Django 4.0.6 on 2022-07-27 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Total'),
        ),
        migrations.AddField(
            model_name='venda',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Total'),
        ),
    ]
