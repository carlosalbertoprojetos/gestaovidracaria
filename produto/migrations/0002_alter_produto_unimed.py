# Generated by Django 4.0.6 on 2022-07-25 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='unimed',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='produto.unidademedida', verbose_name='Unidade de medida'),
        ),
    ]
