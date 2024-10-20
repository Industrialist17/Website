# Generated by Django 5.1.1 on 2024-10-14 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0009_profile_first_name_profile_last_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='C:\\Users\\Owner\\Desktop\\code.py\\Game\\learning_logs\\images')),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('vsco_url', models.CharField(blank=True, max_length=255, null=True)),
                ('insta_url', models.CharField(blank=True, max_length=255, null=True)),
                ('snapchat_url', models.CharField(blank=True, max_length=255, null=True)),
                ('First_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
