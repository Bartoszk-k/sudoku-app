from django.db import models
from django.contrib.auth.models import User
from .utils import generate_Sudoku
import json
# Create your models here.

class Notes(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Notes")

    def __str__(self):
        return self.Title 
    

def default_boards():
    empty_board = [[0 for _ in range(9)] for _ in range(9)]
    return {
        "completed": empty_board,
        "board": empty_board
    }

class SudokuModel(models.Model):
    Boards = models.JSONField(default=default_boards)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="SudokuView")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate(self):
        self.Boards = generate_Sudoku()
        self.save()