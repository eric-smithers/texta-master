# Generated by Django 2.2.19 on 2021-04-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagger', '0020_stop_words_reformat'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagger',
            name='ignore_numbers',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
