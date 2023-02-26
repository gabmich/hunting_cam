# Generated by Django 4.1.7 on 2023-02-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_behaviour_speed_animaltocrossing_crossing_animals'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Animal', 'verbose_name_plural': 'Animaux'},
        ),
        migrations.AlterModelOptions(
            name='animaltocrossing',
            options={'verbose_name': "Passage d'animal", 'verbose_name_plural': "Passage d'animaux"},
        ),
        migrations.AlterModelOptions(
            name='behaviour',
            options={'verbose_name': 'Comportement'},
        ),
        migrations.AlterModelOptions(
            name='camera',
            options={'verbose_name': 'Caméra'},
        ),
        migrations.AlterModelOptions(
            name='crossing',
            options={'verbose_name': 'Passage'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Lieux', 'verbose_name_plural': 'Lieux'},
        ),
        migrations.AlterModelOptions(
            name='speed',
            options={'verbose_name': 'Vitesse'},
        ),
        migrations.AddField(
            model_name='crossing',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='crossing',
            name='temperature',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
