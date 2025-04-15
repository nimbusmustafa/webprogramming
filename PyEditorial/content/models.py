from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser


class BlogCategory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Blog Category')
        verbose_name_plural = _('Blog Categories')

    def __str__(self):
        return self.title


class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Tech'),
        ('life', 'Lifestyle'),
        ('news', 'News'),
        ('health', 'Health'),
        ('edu', 'Education'),
        ('other', 'Other'),
    ]

    title = models.CharField(
        max_length=256,
        verbose_name='Title',
        unique=True,
        default='Untitled Blog'
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name='Slug',
        unique=True,
        default='untitled-blog'
    )
    thumbnail = models.ImageField(
        upload_to='content/blog/thumbnail/',
        verbose_name='Thumbnail',
        default='default-thumbnail.png'
    )
    publish = models.BooleanField(
        verbose_name='Publish',
        default=True,
        help_text='Will this post be published?'
    )
    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name='Category'
    )
    content = RichTextUploadingField(
        default='Write your blog content here...'
    )

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def display_category(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, 'Unknown')

    def __str__(self):
        return self.title


class VideocastCategory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Video Cast Category')
        verbose_name_plural = _('Video Cast Categories')

    def __str__(self):
        return self.title


class Videocast(models.Model):
    CATEGORY_CHOICES = [
        ('tutorial', 'Tutorial'),
        ('lecture', 'Lecture'),
        ('interview', 'Interview'),
        ('demo', 'Demo'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        default='Untitled Video'
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug :'),
        unique=True,
        default='untitled-video'
    )
    thumbnail = models.ImageField(
        upload_to='content/video/thumbnail/',
        verbose_name=_('Thumbnail :'),
        default='default-video-thumbnail.png'
    )
    publish = models.BooleanField(
        verbose_name=_('Publish :'),
        default=True,
        help_text=_('Will this video be published?')
    )
    video = models.CharField(
        max_length=256,
        verbose_name=_('Video link :'),
        default='https://www.youtube.com/embed/dQw4w9WgXcQ'
    )
    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name=_('Category :')
    )
    content = RichTextUploadingField(
        default='Write your video description here...'
    )

    class Meta:
        verbose_name = _('Video Cast')
        verbose_name_plural = _('Video Casts')

    def display_category(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, 'Unknown')

    def __str__(self):
        return self.title


class PodcastCategory(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = _('Podcast Category')
        verbose_name_plural = _('Podcast Categories')

    def __str__(self):
        return self.title


class Podcast(models.Model):
    CATEGORY_CHOICES = [
        ('talk', 'Talk Show'),
        ('interview', 'Interview'),
        ('educational', 'Educational'),
        ('news', 'News'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        default='Untitled Podcast'
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug :'),
        unique=True,
        default='untitled-podcast'
    )
    thumbnail = models.ImageField(
        upload_to='content/podcast/thumbnail/',
        verbose_name=_('Thumbnail :'),
        default='default-podcast-thumbnail.png'
    )
    publish = models.BooleanField(
        verbose_name=_('Publish :'),
        default=True,
        help_text=_('Will this audio be published?')
    )
    audio = models.CharField(
        max_length=256,
        verbose_name=_('Video link :'),
        default='https://www.youtube.com/embed/dQw4w9WgXcQ'
    )
    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        default='other',
        verbose_name=_('Category :')
    )
    content = RichTextUploadingField(
        default='Write your podcast description here...'
    )

    class Meta:
        verbose_name = _('Podcast')
        verbose_name_plural = _('Podcasts')

    def display_category(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, 'Unknown')

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name=_('Description :'),
        null=False,
        blank=False
    )
    icon = models.CharField(
        max_length=30,
        verbose_name=_('Icon name :'),
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    # Additional fields
    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Add related_name to avoid clashes with default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True
    )
    
    def __str__(self):
        return self.username