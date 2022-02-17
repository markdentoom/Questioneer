from questions.api.permissions import IsAuthorOrReadOnly
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Answer, Question
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


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


class AnswerRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "uuid"


class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug_kwarg = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=slug_kwarg).order_by(
            "-created_at"
        )


class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, uuid):
        return self.post_or_delete(request, uuid)

    def delete(self, request, uuid):
        return self.post_or_delete(request, uuid, remove=True)

    def post_or_delete(self, request, uuid, remove=False):
        answer = get_object_or_404(Answer, uuid=uuid)
        if remove:
            answer.voters.remove(request.user)
        else:
            answer.voters.add(request.user)
        answer.save()
        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
