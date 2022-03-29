# Generated by Django 4.0.3 on 2022-03-29 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_remove_departamento_id_alter_departamento_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('codigoMateria', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cargaHoraria', models.CharField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='materia',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myapi.departamento'),
        ),
    ]