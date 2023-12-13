# Generated by Django 2.2.20 on 2023-12-12 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('APP', '0011_auto_20231212_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=500)),
                ('idade', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('cpf', models.CharField(editable=False, max_length=12, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=500)),
                ('quantQuarto', models.PositiveIntegerField(default=0)),
                ('temQuarto', models.BooleanField(default=False)),
                ('localizacao', models.CharField(default=0, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('numero', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('camasSolteiro', models.PositiveIntegerField()),
                ('ocupado', models.BooleanField(default=False)),
                ('camasCasal', models.PositiveIntegerField()),
                ('idHotel', models.OneToOneField(default=0, on_delete=django.db.models.deletion.PROTECT, to='APP.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('dataEntrada', models.DateField(default=0)),
                ('dataSaida', models.DateField(default=0)),
                ('emAtividade', models.BooleanField(default=False)),
                ('id_Hotel', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='APP.Hotel')),
                ('id_cliente', models.OneToOneField(default=0, on_delete=django.db.models.deletion.PROTECT, to='APP.Cliente')),
                ('id_quarto', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='APP.Quarto')),
            ],
        ),
    ]