from django.core.validators import slug_re
from django.http import request
from rest_framework import generics, serializers, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerCreateView(generics.CreateAPIView):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = generics.get_object_or_404(Question, slug=kwarg_slug)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have answered the question.")
        serializer.save(author=request_user, question=question)
