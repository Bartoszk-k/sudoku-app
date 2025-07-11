from django.urls import path
from . import views
urlpatterns = [
    path("notes/",views.NoteListCreate.as_view(),name="note-list"),
    path("notes/delete/<int:pk>/",views.NoteDelete.as_view(),name="delete-note"),
    path("sudoku/",views.SudokuView.as_view(),name="sudoku"),
    path("sudoku/delete/<int:pk>/",views.SudokuDelete.as_view(),name="delete-sudoku"),
    path("sudoku/save/<int:pk>",views.SudokuSave.as_view(),name="sudoku-save"),
    ]