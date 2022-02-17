from rest_framework import generics, viewsets
from questions.models import Answer, Question
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from rest_framework.permissions import IsAuthenticated
from questions.api.permissions import IsAuthorOrReadOnly
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        slug_kwarg = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=slug_kwarg)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this question")
        serializer.save(author=request_user, question=question)
