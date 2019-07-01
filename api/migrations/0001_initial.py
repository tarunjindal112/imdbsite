# Generated by Django 2.2.1 on 2019-06-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('imdb_score', models.FloatField()),
                ('popularity', models.FloatField()),
                ('director', models.CharField(max_length=500)),
                ('genre', models.ManyToManyField(to='api.Genre')),
            ],
        ),
    ]