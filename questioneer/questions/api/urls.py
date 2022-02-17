from django.urls import path, include
from rest_framework.routers import DefaultRouter
from questions.api import views as question_views

router = DefaultRouter()
router.register(r"questions", question_views.QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "questions/<slug:slug>/answer/",
        question_views.AnswerCreateAPIView.as_view(),
        name="answer-create",
    ),
    path(
        "questions/<slug:slug>/answers/",
        question_views.AnswerListAPIView.as_view(),
        name="answer-list",
    ),
    path(
        "answers/<uuid:uuid>/",
        question_views.AnswerRetrieveUpdateDestroyAPIView.as_view(),
        name="answer-detail",
    ),
]
