from pytils.translit import slugify

from django import forms
from django.core.exceptions import ValidationError

from .models import Note

WARNING = '- un slug así ya existe, ¡crea un valor único!'


class NoteForm(forms.ModelForm):
    """Formulario para crear o actualizar una nota."""

    class Meta:
        model = Note
        fields = ('title', 'text', 'slug')

    def clean_slug(self):
        """Procesa los casos en los que el slug no es único."""
        cleaned_data = super().clean()
        slug = cleaned_data.get('slug')
        if not slug:
            title = cleaned_data.get('title')
            slug = Note.get_slug_by_title(title)
        if Note.objects.filter(
                slug=slug
        ).exclude(id=self.instance.pk).exists():
            raise ValidationError(slug + WARNING)
        return slug
