# Generated by Django 3.1.4 on 2020-12-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_link', models.CharField(max_length=255)),
                ('insta_link', models.CharField(max_length=255)),
                ('twitter_link', models.CharField(max_length=255)),
                ('yt_link', models.CharField(max_length=255)),
                ('all_rights_msg', models.CharField(max_length=255)),
                ('tuber_hire', models.CharField(max_length=255)),
            ],
        ),
    ]
