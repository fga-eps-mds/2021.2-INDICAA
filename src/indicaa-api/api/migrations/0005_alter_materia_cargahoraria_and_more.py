# Generated by Django 4.0.3 on 2022-04-23 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_materia_cargahoraria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='cargaHoraria',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='materia',
            name='codigoMateria',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='turma',
            name='codigoTurma',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='turma',
            name='horario',
            field=models.CharField(max_length=170),
        ),
    ]
