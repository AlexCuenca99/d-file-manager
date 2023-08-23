import os
import uuid
from django.db import models
from django.contrib.auth import get_user_model

from model_utils.models import TimeStampedModel

from .utils import set_file_path

User = get_user_model()


class File(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField("File", upload_to=set_file_path, max_length=100)
    owner = models.ForeignKey(User, related_name="files", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

    def get_file_name(self):
        return os.path.basename(self.file.name)

    def get_file_extension(self):
        return self.get_file_name().split(".")[-1]

    def __str__(self) -> str:
        return self.file.name
