# Generated by Django 4.1.7 on 2023-03-11 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_video_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animaltocrossing',
            name='speed',
        ),
    ]
