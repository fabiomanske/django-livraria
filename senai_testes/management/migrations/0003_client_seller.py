# Generated by Django 5.0.7 on 2024-08-01 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_user_created_at_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('phone', models.CharField(help_text='Telefone principal para contato', max_length=50, verbose_name='Telefone')),
                ('cpf', models.CharField(blank=True, max_length=20, null=True, verbose_name='CPF')),
                ('address', models.CharField(help_text='Endereço oficial', max_length=100, verbose_name='Endereço')),
                ('address_number', models.CharField(max_length=50, verbose_name='Número')),
                ('address_complement', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Complemento')),
                ('city', models.CharField(help_text='Cidade', max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('DF', 'Distrito Federal')], help_text='Estado da federação', max_length=2, verbose_name='Estado')),
                ('zipcode', models.CharField(help_text='CEP', max_length=20)),
                ('user', models.OneToOneField(help_text='Usuário', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('phone', models.CharField(help_text='Telefone principal para contato', max_length=50, verbose_name='Telefone')),
                ('cpf', models.CharField(blank=True, max_length=20, null=True, verbose_name='CPF')),
                ('hiring_date', models.DateField(help_text='Data de contratação', verbose_name='Data de contratação')),
                ('birthday', models.DateField(help_text='Data de nascimento', verbose_name='Data de nascimento')),
                ('user', models.OneToOneField(help_text='Usuário', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Vendedor',
                'verbose_name_plural': 'Vendedores',
            },
        ),
    ]
