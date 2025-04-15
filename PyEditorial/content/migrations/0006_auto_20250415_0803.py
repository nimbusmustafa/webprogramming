# Generated by Django 3.2.21 on 2025-04-15 08:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20250415_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='audio',
            field=models.FileField(default='default-audio.mp3', upload_to='content/podcast/audio/', verbose_name='Audio :'),
        ),
        migrations.RemoveField(
            model_name='podcast',
            name='category',
        ),
        migrations.AddField(
            model_name='podcast',
            name='category',
            field=models.CharField(choices=[('talk', 'Talk Show'), ('interview', 'Interview'), ('educational', 'Educational'), ('news', 'News'), ('entertainment', 'Entertainment'), ('other', 'Other')], default='other', max_length=32, verbose_name='Category :'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Write your podcast description here...'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='slug',
            field=models.SlugField(default='untitled-podcast', max_length=256, unique=True, verbose_name='Slug :'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='thumbnail',
            field=models.ImageField(default='default-podcast-thumbnail.png', upload_to='content/podcast/thumbnail/', verbose_name='Thumbnail :'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='title',
            field=models.CharField(default='Untitled Podcast', max_length=256, unique=True, verbose_name='Title :'),
        ),
        migrations.RemoveField(
            model_name='videocast',
            name='category',
        ),
        migrations.AddField(
            model_name='videocast',
            name='category',
            field=models.CharField(choices=[('tutorial', 'Tutorial'), ('lecture', 'Lecture'), ('interview', 'Interview'), ('demo', 'Demo'), ('entertainment', 'Entertainment'), ('other', 'Other')], default='other', max_length=32, verbose_name='Category :'),
        ),
        migrations.AlterField(
            model_name='videocast',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Write your video description here...'),
        ),
        migrations.AlterField(
            model_name='videocast',
            name='slug',
            field=models.SlugField(default='untitled-video', max_length=256, unique=True, verbose_name='Slug :'),
        ),
        migrations.AlterField(
            model_name='videocast',
            name='thumbnail',
            field=models.ImageField(default='default-video-thumbnail.png', upload_to='content/video/thumbnail/', verbose_name='Thumbnail :'),
        ),
        migrations.AlterField(
            model_name='videocast',
            name='title',
            field=models.CharField(default='Untitled Video', max_length=256, unique=True, verbose_name='Title :'),
        ),
        migrations.AlterField(
            model_name='videocast',
            name='video',
            field=models.CharField(default='https://www.youtube.com/embed/dQw4w9WgXcQ', max_length=256, verbose_name='Video link :'),
        ),
    ]
