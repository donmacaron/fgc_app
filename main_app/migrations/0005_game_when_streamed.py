# Generated by Django 2.2.7 on 2020-01-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20191018_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='when_streamed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
