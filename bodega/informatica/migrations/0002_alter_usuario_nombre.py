# Generated by Django 5.1.1 on 2024-12-01 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informatica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
