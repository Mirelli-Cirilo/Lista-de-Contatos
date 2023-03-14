# Generated by Django 4.1.7 on 2023-03-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=250)),
                ('relação', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('numero', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=200)),
            ],
        ),
    ]
