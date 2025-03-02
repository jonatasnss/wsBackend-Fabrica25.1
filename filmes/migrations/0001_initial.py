from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colecoes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Coleção',
                'verbose_name_plural': 'Coleções',
                'ordering': ['-data_criacao'],
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('ano', models.CharField(max_length=10)),
                ('diretor', models.CharField(blank=True, max_length=200)),
                ('genero', models.CharField(blank=True, max_length=200)),
                ('sinopse', models.TextField(blank=True)),
                ('poster_url', models.URLField(blank=True)),
                ('imdb_id', models.CharField(max_length=20, unique=True)),
                ('data_adicao', models.DateTimeField(auto_now_add=True)),
                ('colecoes', models.ManyToManyField(blank=True, related_name='filmes', to='filmes.colecao')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
                'ordering': ['-data_adicao'],
            },
        ),
    ]