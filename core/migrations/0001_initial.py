# Generated by Django 5.1.2 on 2024-10-21 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('thumbnail', models.ImageField(null=True, upload_to='thumbnails/', verbose_name='Miniatura')),
                ('video', models.FileField(null=True, upload_to='videos/', verbose_name='Vídeo')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('published_at', models.DateTimeField(editable=False, null=True, verbose_name='Publicado em')),
                ('is_published', models.BooleanField(default=False, verbose_name='Está publicado?')),
                ('num_likes', models.IntegerField(default=0, editable=False, verbose_name='Número de curtidas')),
                ('num_views', models.IntegerField(default=0, editable=False, verbose_name='Número de visualizações')),
                ('tags', models.ManyToManyField(to='core.tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Vídeo',
                'verbose_name_plural': 'Vídeos',
            },
        ),
    ]
