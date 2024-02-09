# Generated by Django 4.2.10 on 2024-02-09 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0012_remove_thesis_adviser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='thesis',
            name='adviser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='searcher.adviser'),
            preserve_default=False,
        ),
    ]
