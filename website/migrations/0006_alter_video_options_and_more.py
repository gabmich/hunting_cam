# Generated by Django 4.1.7 on 2023-03-11 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_crossing_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Vidéo'},
        ),
        migrations.RenameField(
            model_name='animaltocrossing',
            old_name='crossing',
            new_name='video',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='video',
            new_name='videofile',
        ),
    ]
