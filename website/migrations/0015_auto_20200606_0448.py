# Generated by Django 3.0.7 on 2020-06-06 07:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20200606_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 7, 48, 57, 40600, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 7, 48, 57, 40600, tzinfo=utc)),
        ),
    ]
