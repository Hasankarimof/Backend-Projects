# Generated by Django 5.0.6 on 2024-07-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookListAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='inventory',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
