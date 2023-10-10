from django.conf import settings
from django.db import models

from pytils.translit import slugify


class Note(models.Model):
    title = models.CharField(
        'Title',
        max_length=100,
        default='Title of note',
        help_text='Give a short title to the note'
    )
    text = models.TextField(
        'Body',
        help_text='Add more details'
    )
    slug = models.SlugField(
        'Address for the page with a note',
        max_length=100,
        unique=True,
        blank=True,
        help_text=('Indicate the address for the note page. Use only '
                   'Latin characters, numbers, hyphens and underscores')
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug_by_title(self.title)
        super().save(*args, **kwargs)

    @classmethod
    def get_slug_by_title(cls, title):
        """Creating a slug for a note based on the title."""
        max_slug_length = cls._meta.get_field('slug').max_length
        return slugify(title)[:max_slug_length]
