# Generated by Django 3.0 on 2020-06-13 15:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20200606_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 15, 46, 42, 155245, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 15, 46, 42, 156280, tzinfo=utc)),
        ),
    ]
