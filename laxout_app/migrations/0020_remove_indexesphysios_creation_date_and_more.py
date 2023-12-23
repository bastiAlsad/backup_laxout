# Generated by Django 5.0 on 2023-12-16 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxout_app', '0019_alter_indexeslaxoutuser_creation_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexesphysios',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='indexesphysios',
            name='for_month',
            field=models.IntegerField(default=12),
        ),
        migrations.AddField(
            model_name='indexesphysios',
            name='logins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='indexesphysios',
            name='tests',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='indexeslaxoutuser',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 16, 16, 52, 43, 306269, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 16, 16, 52, 43, 307269, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='user_uid',
            field=models.CharField(default='b40d5f7a-c0f2-4c55-baa3-154f095c6d55', max_length=420, unique=True),
        ),
    ]
