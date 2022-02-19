import uuid as uuid_lib

from core.models import TimeStampedModel
from django.conf import settings
from django.db import models


class Question(TimeStampedModel):
    uuid = models.UUIDField(editable=False, default=uuid_lib.uuid4)
    content = models.CharField(max_length=240)
    # 15 characters more than content so we can add a unique random identifier at the end
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    def __str__(self) -> str:
        return str(self.content)


class Answer(TimeStampedModel):
    # Use uuid instead of id/ pk for safety reasons
    uuid = models.UUIDField(
        db_index=True, editable=False, default=uuid_lib.uuid4
    )
    body = models.TextField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    voters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="likes"
    )

    def __str__(self) -> str:
        return str(self.author.username)
