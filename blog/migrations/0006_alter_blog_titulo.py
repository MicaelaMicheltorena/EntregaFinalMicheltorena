# Generated by Django 4.0.3 on 2022-04-11 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_autor_alter_blog_subtitulo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]
