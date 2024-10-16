# Generated by Django 5.1.1 on 2024-10-12 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='categories.genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
