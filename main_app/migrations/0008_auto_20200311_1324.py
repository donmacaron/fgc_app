# Generated by Django 3.0.3 on 2020-03-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200221_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover',
            field=models.ImageField(default='/images/default.jpg', upload_to='images/covers'),
        ),
    ]