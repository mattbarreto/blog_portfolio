# Generated by Django 4.0.4 on 2022-04-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_description_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Publicado/No publicado'),
        ),
    ]
