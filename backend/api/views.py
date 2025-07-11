from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, Noteserializer, SudokuSerializer
from.models import Notes, SudokuModel
from rest_framework.permissions import IsAuthenticated, AllowAny
from .utils import generate_Sudoku
import json

# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = Noteserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):

    serializer_class = Noteserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author = user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class SudokuView(generics.ListCreateAPIView):
    serializer_class = SudokuSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return SudokuModel.objects.filter(author=user)

    def perform_create(self, serializer):
        generated_board = generate_Sudoku()
        serializer.save(author=self.request.user, Boards = generated_board)

class SudokuDelete(generics.DestroyAPIView):
    serializer_class = SudokuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return SudokuModel.objects.filter(author = user)
    
class SudokuSave(generics.UpdateAPIView):
    serializer_class = SudokuSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)