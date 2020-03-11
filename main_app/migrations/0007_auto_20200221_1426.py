# Generated by Django 2.2.6 on 2020-02-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_game_stream_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover',
            field=models.ImageField(default='img/carousel/wii.jpg', upload_to='images/covers'),
        ),
        migrations.AlterField(
            model_name='game',
            name='stream_list',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
