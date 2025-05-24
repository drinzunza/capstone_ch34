from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Note
from .forms import NoteForm
from django.urls import reverse_lazy

"""
Class-based views:

View        = generic view
ListView    = get a list of records
DetailView  = get a single(detail) record
CreateView  = create a new record
DeleteView  = remove a record
UpdateView  = modify an existing record
LoginView   = login
"""

# Create your views here.
class NoteList(ListView):
    model = Note
    template_name = "notes/list.html"


class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/create.html"
    success_url = reverse_lazy('note_list')

    def get_context_data(self, **kwargs):
        # allow us to extend/modify the context pass to the template
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Note"
        return context



class NoteDetail(DetailView):
    model = Note
    template_name = "notes/details.html"



class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/create.html"
    success_url = reverse_lazy('note_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Note"
        return context
    



class NoteDelete(DeleteView):
    model = Note
    template_name = "notes/delete.html"
    success_url = reverse_lazy('note_list')
