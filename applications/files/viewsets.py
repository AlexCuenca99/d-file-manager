from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import File
from .serializers import FileModelSerializer


class FileModelViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
