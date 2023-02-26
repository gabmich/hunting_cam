# Generated by Django 4.1.7 on 2023-02-26 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_camera_crossing_camera'),
    ]

    operations = [
        migrations.CreateModel(
            name='Behaviour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalToCrossing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.animal')),
                ('behaviour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.behaviour')),
                ('crossing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.crossing')),
                ('speed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.speed')),
            ],
        ),
        migrations.AddField(
            model_name='crossing',
            name='animals',
            field=models.ManyToManyField(through='website.AnimalToCrossing', to='website.animal'),
        ),
    ]
