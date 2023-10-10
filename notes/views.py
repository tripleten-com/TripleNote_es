from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import NoteForm
from .models import Note


class Home(generic.TemplateView):
    """Homepage."""
    template_name = 'notes/home.html'


class NoteSuccess(LoginRequiredMixin, generic.TemplateView):
    """Success page for completed operation."""
    template_name = 'notes/success.html'


class NoteBase(LoginRequiredMixin):
    """Base class for the rest of the CBVs."""
    model = Note
    success_url = reverse_lazy('notes:success')

    def get_queryset(self):
        """The user can only work with their own notes."""
        return self.model.objects.filter(author=self.request.user)


class NoteCreate(NoteBase, generic.CreateView):
    """Adding a note."""
    template_name = 'notes/form.html'
    form_class = NoteForm

    def form_valid(self, form):
        new_note = form.save(commit=False)
        new_note.author = self.request.user
        new_note.save()
        return super().form_valid(form)


class NoteUpdate(NoteBase, generic.UpdateView):
    """Editing a note."""
    template_name = 'notes/form.html'
    form_class = NoteForm


class NoteDelete(NoteBase, generic.DeleteView):
    """Deleting a note."""
    template_name = 'notes/delete.html'


class NotesList(NoteBase, generic.ListView):
    """List of all user's notes."""
    template_name = 'notes/list.html'


class NoteDetail(NoteBase, generic.DetailView):
    """The note is detailed."""
    template_name = 'notes/detail.html'
