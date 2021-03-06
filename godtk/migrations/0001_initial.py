# Generated by Django 3.0.3 on 2020-03-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Godtk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('title_en', models.CharField(max_length=40)),
                ('audience', models.IntegerField()),
                ('open_date', models.IntegerField()),
                ('genre', models.TextField()),
                ('watch_grade', models.TextField()),
                ('score', models.FloatField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
