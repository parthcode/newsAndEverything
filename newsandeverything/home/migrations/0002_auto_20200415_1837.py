# Generated by Django 2.2.4 on 2020-04-15 13:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 13, 7, 6, 598592, tzinfo=utc)),
        ),
    ]