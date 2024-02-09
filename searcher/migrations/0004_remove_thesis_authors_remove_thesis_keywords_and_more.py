# Generated by Django 4.2.10 on 2024-02-09 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0003_alter_thesis_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='thesis',
            name='panelists',
        ),
        migrations.AddField(
            model_name='author',
            name='thesis',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='theses', to='searcher.thesis'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.DeleteModel(
            name='Panelist',
        ),
    ]
