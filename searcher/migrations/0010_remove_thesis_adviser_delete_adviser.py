# Generated by Django 4.2.10 on 2024-02-09 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0009_adviser_alter_thesis_adviser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='adviser',
        ),
        migrations.DeleteModel(
            name='Adviser',
        ),
    ]
