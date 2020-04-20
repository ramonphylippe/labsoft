# Generated by Django 3.0.5 on 2020-04-19 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarioNome', models.CharField(blank='false', max_length=16, verbose_name='Nome')),
                ('sobrenome', models.CharField(blank='false', max_length=16, verbose_name='Sobrenome')),
                ('cpf', models.DecimalField(decimal_places=0, max_digits=11, verbose_name='Cpf')),
                ('contato1', models.DecimalField(blank='false', decimal_places=0, max_digits=12, verbose_name='telefone - principal')),
                ('cep', models.DecimalField(blank='false', decimal_places=0, max_digits=8, verbose_name='Cep')),
                ('usuarioEmail', models.EmailField(blank='false', max_length=64, unique='true', verbose_name='email')),
                ('usuarioSenha', models.CharField(blank='false', max_length=32, verbose_name='senha')),
                ('usuarioStatus', models.BooleanField(default='True', verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produtoNome', models.CharField(blank='false', max_length=16, verbose_name='Nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('estoque', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='estoque')),
                ('produtoStatus', models.BooleanField(default='true', verbose_name='Produto ativo')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Usuario')),
            ],
        ),
    ]