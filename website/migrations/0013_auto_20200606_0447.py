# Generated by Django 3.0.7 on 2020-06-06 07:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200606_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 7, 47, 2, 36888, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 7, 47, 2, 36888, tzinfo=utc)),
        ),
    ]
