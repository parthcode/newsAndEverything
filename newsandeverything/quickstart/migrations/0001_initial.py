# Generated by Django 3.1.4 on 2021-01-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('urlToImage', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('dateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
