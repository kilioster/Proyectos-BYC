# Generated by Django 5.1.2 on 2024-11-13 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0003_rename_casas_casa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casa',
            name='baths',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='casa',
            name='rooms',
            field=models.IntegerField(default='1'),
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.FileField(upload_to='images/')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='propiedades.casa')),
            ],
        ),
    ]
