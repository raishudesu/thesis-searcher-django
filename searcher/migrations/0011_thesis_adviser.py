# Generated by Django 4.2.10 on 2024-02-09 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0010_remove_thesis_adviser_delete_adviser'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='adviser',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
