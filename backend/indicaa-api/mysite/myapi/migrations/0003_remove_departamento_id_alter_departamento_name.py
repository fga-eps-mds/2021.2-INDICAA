# Generated by Django 4.0.3 on 2022-03-29 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_departamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='id',
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
