# Generated by Django 4.1.2 on 2022-10-10 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe_app', '0008_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 10, 16, 59, 58, 337489)),
        ),
    ]