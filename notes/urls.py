from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.NoteList.as_view(), name="note_list"),
    path('create/', views.NoteCreate.as_view(), name="note_create"),
    path('details/<int:pk>/', views.NoteDetail.as_view(), name="note_details"),
    path('update/<int:pk>/', views.NoteUpdate.as_view(), name="note_update"),
    path('delete/<int:pk>/', views.NoteDelete.as_view(), name="note_delete"),
    path('save_comment/', views.save_comment, name="save_comment"),
]
