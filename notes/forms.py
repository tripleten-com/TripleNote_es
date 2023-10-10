from pytils.translit import slugify

from django import forms
from django.core.exceptions import ValidationError

from .models import Note

WARNING = ' - such a slug already exists; come up with a unique value!'


class NoteForm(forms.ModelForm):
    """Form for creating or updating a note."""

    class Meta:
        model = Note
        fields = ('title', 'text', 'slug')

    def clean_slug(self):
        """Processes the cases where slug is not unique."""
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
