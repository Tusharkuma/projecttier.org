# Generated by Django 2.0.2 on 2018-03-28 19:42

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('exercises', '0003_exercisepage_listing_excerpt'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseLevelTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DisciplineTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProtocolTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='exercisepagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='exercisepagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='exercisepage',
            name='tags',
        ),
        migrations.DeleteModel(
            name='ExercisePageTag',
        ),
        migrations.AddField(
            model_name='protocoltag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='protocol_tags_relationship', to='exercises.ExercisePage'),
        ),
        migrations.AddField(
            model_name='protocoltag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises_protocoltag_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='disciplinetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='discipline_tags_relationship', to='exercises.ExercisePage'),
        ),
        migrations.AddField(
            model_name='disciplinetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises_disciplinetag_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='courseleveltag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_level_tags_relationship', to='exercises.ExercisePage'),
        ),
        migrations.AddField(
            model_name='courseleveltag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises_courseleveltag_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='exercisepage',
            name='course_level_tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='+', through='exercises.CourseLevelTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='exercisepage',
            name='discipline_tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='+', through='exercises.DisciplineTag', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='exercisepage',
            name='protocol_tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', related_name='+', through='exercises.ProtocolTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
