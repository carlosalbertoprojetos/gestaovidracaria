# Generated by Django 4.0.6 on 2022-07-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimento',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
    ]
