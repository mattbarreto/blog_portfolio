# Generated by Django 4.0.4 on 2022-04-20 19:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(auto_now_add=True, verbose_name=datetime.date.today),
        ),
    ]
