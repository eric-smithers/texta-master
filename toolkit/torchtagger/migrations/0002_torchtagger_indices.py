# Generated by Django 2.1.15 on 2020-03-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elastic', '0003_index'),
        ('torchtagger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='torchtagger',
            name='indices',
            field=models.ManyToManyField(default=None, to='elastic.Index'),
        ),
    ]
