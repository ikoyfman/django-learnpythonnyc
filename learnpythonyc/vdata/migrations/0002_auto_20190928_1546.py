# Generated by Django 2.2.5 on 2019-09-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='released',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
