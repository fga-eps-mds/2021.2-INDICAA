# Generated by Django 4.0.3 on 2022-04-20 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_departamento_unidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='codigoTurma',
            field=models.CharField(max_length=4),
        ),
    ]