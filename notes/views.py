from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import NoteForm
from .models import Note


class Home(generic.TemplateView):
    """Página de inicio."""
    template_name = 'notes/home.html'


class NoteSuccess(LoginRequiredMixin, generic.TemplateView):
    """Página de éxito para la operación completada."""
    template_name = 'notes/success.html'


class NoteBase(LoginRequiredMixin):
    """Clase base para el resto de los CBV."""
    model = Note
    success_url = reverse_lazy('notes:success')

    def get_queryset(self):
        """El usuario solo puede trabajar con sus propias notas."""
        return self.model.objects.filter(author=self.request.user)


class NoteCreate(NoteBase, generic.CreateView):
    """Añadir una nota."""
    template_name = 'notes/form.html'
    form_class = NoteForm

    def form_valid(self, form):
        new_note = form.save(commit=False)
        new_note.author = self.request.user
        new_note.save()
        return super().form_valid(form)


class NoteUpdate(NoteBase, generic.UpdateView):
    """Editar una nota."""
    template_name = 'notes/form.html'
    form_class = NoteForm


class NoteDelete(NoteBase, generic.DeleteView):
    """Eliminar una nota."""
    template_name = 'notes/delete.html'


class NotesList(NoteBase, generic.ListView):
    """Lista de todas las notas del usuario."""
    template_name = 'notes/list.html'


class NoteDetail(NoteBase, generic.DetailView):
    """La nota es detallada."""
    template_name = 'notes/detail.html'
