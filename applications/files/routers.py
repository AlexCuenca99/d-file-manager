from rest_framework import routers

from .viewsets import FileModelViewSet


router = routers.DefaultRouter()
router.register(r"files", FileModelViewSet, basename="files")
