from django.conf import settings
from django.db import models

from pytils.translit import slugify


class Note(models.Model):
    title = models.CharField(
        'Título',
        max_length=100,
        default='Título de la nota',
        help_text='Dale un título corto a la nota'
    )
    text = models.TextField(
        'Cuerpo',
        help_text='Añade más detalles'
    )
    slug = models.SlugField(
        'Dirección de la página con una nota',
        max_length=100,
        unique=True,
        blank=True,
        help_text=('Indica la dirección de la página de la nota. Utiliza solo '
                   'caracteres latinos, números, guiones y guiones bajos')
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
        """Crear un slug para una nota basado en el título."""
        max_slug_length = cls._meta.get_field('slug').max_length
        return slugify(title)[:max_slug_length]
