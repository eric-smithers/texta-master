# Generated by Django 2.2.22 on 2021-06-16 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0015_project_administrators'),
        ('elastic', '0012_auto_20210526_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyESAnalyzerWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('query', models.TextField(default='{"query": {"match_all": {}}}')),
                ('fields', models.TextField(default='[]')),
                ('analyzers', models.TextField(default='[]')),
                ('strip_html', models.BooleanField(default=True)),
                ('tokenizer', models.CharField(default='standard', max_length=100)),
                ('stemmer_lang', models.CharField(max_length=100, null=True)),
                ('detect_lang', models.BooleanField(default=False)),
                ('es_timeout', models.IntegerField(default=15, help_text='How many minutes should there be between scroll requests before triggering a timeout.')),
                ('bulk_size', models.IntegerField(default=100, help_text='How many documents should be returned by Elasticsearch with each request.')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('indices', models.ManyToManyField(to='elastic.Index')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
                ('task', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Task')),
            ],
        ),
        migrations.DeleteModel(
            name='ApplyStemmerWorker',
        ),
    ]
