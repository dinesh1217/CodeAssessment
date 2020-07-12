from rest_framework import generics, permissions as rest_per
from rest_framework import viewsets
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from .permissions import ReadOnlyPermission


class QuestionView(viewsets.ModelViewSet):
    permission_classes = [ReadOnlyPermission]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceView(viewsets.ModelViewSet):
    permission_classes = [ReadOnlyPermission]
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


