# Generated by Django 5.1.1 on 2024-10-12 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0007_profile_insta_url_profile_profile_pic_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='website_url',
            new_name='email',
        ),
    ]
