# Generated by Django 2.2.5 on 2019-09-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdata', '0002_auto_20190928_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='na_sales',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
