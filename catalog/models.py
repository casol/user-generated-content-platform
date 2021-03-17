from django.db import models

from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

from nanoid import generate


def generate_custom_url():
    """A tiny, secure, URL-friendly, unique string ID generator for Python."""
    custom_url = generate(
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        8)
    return custom_url


class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='user_content',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    custom_url = models.CharField(blank=True, null=False,
                                  max_length=8, default=generate_custom_url)
    active = models.BooleanField(default=True)
    source_url = models.URLField(blank=True, null=False,
                                 help_text="Content source URL")
    content = models.FileField(upload_to='content/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)
    users_score = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                         related_name='content_score',
                                         blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('content_detail', args=[str(self.custom_url)])
