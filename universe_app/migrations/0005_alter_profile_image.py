# Generated by Django 4.1.1 on 2022-09-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe_app', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default/profile2.jpg', upload_to='profile_pics'),
        ),
    ]