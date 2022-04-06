# Generated by Django 4.0.3 on 2022-03-31 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigoMateria', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('cargaHoraria', models.CharField(max_length=3)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('idTurma', models.AutoField(primary_key=True, serialize=False)),
                ('docente', models.CharField(max_length=255)),
                ('codigoTurma', models.CharField(max_length=2)),
                ('horario', models.CharField(max_length=20)),
                ('vagasOfertadas', models.IntegerField()),
                ('vagasOcupadas', models.IntegerField()),
                ('local', models.CharField(max_length=255)),
                ('semestre', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.materia')),
            ],
        ),
    ]