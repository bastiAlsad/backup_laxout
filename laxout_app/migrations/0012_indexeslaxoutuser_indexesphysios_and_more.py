# Generated by Django 5.0 on 2023-12-12 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxout_app', '0011_remove_userprofile_physios_exercises_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexesLaxoutUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('creation_date', models.DateField(default=datetime.datetime(2023, 12, 12, 17, 35, 38, 96721, tzinfo=datetime.timezone.utc))),
                ('created_by', models.IntegerField(blank=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='IndexesPhysios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('creation_date', models.DateField(default=datetime.datetime(2023, 12, 12, 17, 35, 38, 96721, tzinfo=datetime.timezone.utc))),
                ('created_by', models.IntegerField(blank=True, default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 12, 17, 35, 38, 97724, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='user_uid',
            field=models.CharField(default='54a5535c-85ba-4036-9833-ef83a3698827', max_length=420, unique=True),
        ),
        migrations.AddField(
            model_name='laxoutuser',
            name='indexes',
            field=models.ManyToManyField(to='laxout_app.indexeslaxoutuser'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='indexes',
            field=models.ManyToManyField(to='laxout_app.indexesphysios'),
        ),
    ]
