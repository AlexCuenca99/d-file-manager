from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import File
from .serializers import FileModelSerializer


class MyFilesListApiView(generics.ListAPIView):
    """
    Returns a list of all request user files.
    """

    serializer_class = FileModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)
