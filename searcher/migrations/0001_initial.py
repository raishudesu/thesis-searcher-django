# Generated by Django 4.2.10 on 2024-02-08 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Panelist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('abstract', models.TextField()),
                ('status', models.CharField(choices=[('RJ', 'Rejected'), ('PB', 'Published'), ('UR', 'Under Review')], default='UR', max_length=3)),
                ('defense_date', models.DateTimeField()),
                ('published_date', models.DateTimeField()),
                ('paper_link', models.CharField(max_length=250)),
                ('institution', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
                ('adviser', models.CharField(max_length=250)),
                ('authors', models.ManyToManyField(related_name='theses', to='searcher.author')),
                ('keywords', models.ManyToManyField(related_name='theses', to='searcher.keyword')),
                ('panelists', models.ManyToManyField(related_name='theses', to='searcher.panelist')),
            ],
        ),
    ]