# Generated by Django 3.0.7 on 2021-01-31 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200118_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_avatar.png', null=True, upload_to='users/'),
        ),
    ]
