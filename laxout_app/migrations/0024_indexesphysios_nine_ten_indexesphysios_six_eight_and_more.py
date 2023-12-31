# Generated by Django 5.0 on 2023-12-17 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxout_app', '0023_rename_index_indexesphysios_indexs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexesphysios',
            name='nine_ten',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='indexesphysios',
            name='six_eight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='indexesphysios',
            name='theree_five',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='indexesphysios',
            name='zero_two',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 17, 16, 12, 3, 580904, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='user_uid',
            field=models.CharField(default='6fb8688d-2905-4f49-927e-60110a96b07e', max_length=420, unique=True),
        ),
    ]
