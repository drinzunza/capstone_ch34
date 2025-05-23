from django.shortcuts import render
from django.views.generic import ListView, CreateView
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