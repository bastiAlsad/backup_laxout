# Generated by Django 5.0 on 2023-12-10 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxout_app', '0008_alter_laxoutuser_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laxoutuser',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 10, 22, 12, 22, 789753, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='user_uid',
            field=models.CharField(default='L70qhCDweQWIHIVVf9C7d7HVZS6DBjqhuGgffhFkC6DNMnm1Ui2fZmWQ1iub8WDDLnk53Q', max_length=420, unique=True),
        ),
    ]
