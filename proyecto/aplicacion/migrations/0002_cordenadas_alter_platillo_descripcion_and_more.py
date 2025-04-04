# Generated by Django 5.1.7 on 2025-03-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cordenadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='platillo',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='platillo',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
