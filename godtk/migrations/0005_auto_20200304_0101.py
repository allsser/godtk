# Generated by Django 3.0.3 on 2020-03-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('godtk', '0004_auto_20200303_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='godtk',
            old_name='description',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='godtk',
            name='event_title',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='godtk',
            name='hashtag',
            field=models.ManyToManyField(blank=True, to='godtk.Hashtag'),
        ),
    ]
