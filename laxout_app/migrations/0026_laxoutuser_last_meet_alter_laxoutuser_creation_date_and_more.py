# Generated by Django 5.0 on 2023-12-21 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxout_app', '0025_remove_userprofile_average_pain_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laxoutuser',
            name='last_meet',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 21, 17, 9, 43, 460299, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='user_uid',
            field=models.CharField(default='c89cec94-9a29-40ea-9b63-11cd9bf4c866', max_length=420, unique=True),
        ),
    ]
