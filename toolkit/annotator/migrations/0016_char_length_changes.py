# Generated by Django 2.2.28 on 2022-08-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0015_reformat_tasks_and_es_timeouts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotator',
            name='annotation_type',
            field=models.CharField(choices=[('binary', 'binary'), ('multilabel', 'multilabel'), ('entity', 'entity')], help_text='Which type of annotation does the user wish to perform', max_length=255),
        ),
        migrations.AlterField(
            model_name='annotator',
            name='annotator_uid',
            field=models.CharField(default='', help_text='Unique Identifier for Annotator', max_length=255),
        ),
        migrations.AlterField(
            model_name='annotator',
            name='target_field',
            field=models.CharField(default='', help_text='Which Elasticsearch document field you use base the annotation on.', max_length=255),
        ),
        migrations.AlterField(
            model_name='binaryannotatorconfiguration',
            name='fact_name',
            field=models.CharField(help_text='Sets the value for the fact name for all annotated documents.', max_length=255),
        ),
        migrations.AlterField(
            model_name='binaryannotatorconfiguration',
            name='neg_value',
            field=models.CharField(help_text='Sets the name for a fact value for negative documents.', max_length=255),
        ),
        migrations.AlterField(
            model_name='binaryannotatorconfiguration',
            name='pos_value',
            field=models.CharField(help_text='Sets the name for a fact value for positive documents.', max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='value',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='document_id',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='entityannotatorconfiguration',
            name='fact_name',
            field=models.CharField(help_text='Name of the fact which will be added.', max_length=255),
        ),
        migrations.AlterField(
            model_name='label',
            name='value',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='document_id',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='record',
            name='index',
            field=models.CharField(max_length=255),
        ),
    ]
