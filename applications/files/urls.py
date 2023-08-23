from django.urls import include, path

from .routers import router
from .views import MyFilesListApiView

app_name = "files"


urlpatterns = [
    path("", include(router.urls)),
    path("my-files/", MyFilesListApiView.as_view(), name="my-files"),
]
