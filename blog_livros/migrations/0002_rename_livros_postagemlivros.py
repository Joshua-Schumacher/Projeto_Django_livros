# Generated by Django 5.2.1 on 2025-06-02 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_livros', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Livros',
            new_name='PostagemLivros',
        ),
    ]
