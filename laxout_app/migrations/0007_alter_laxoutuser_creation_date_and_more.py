# Generated by Django 5.0 on 2023-12-10 22:04

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laxout_app', '0006_alter_laxoutuser_creation_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='laxoutuser',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 10, 22, 4, 37, 859347, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='laxoutuser',
            name='user_uid',
            field=models.CharField(default='dmjTccpqmC9880LSSnyzxBS999oq4YVAiMI94OxeXhvwLBwRHHtow00HByuBl3LDMFTG2Q', max_length=420, unique=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physios_exercises', models.ManyToManyField(to='laxout_app.laxout_exercise')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
