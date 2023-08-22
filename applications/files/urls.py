from django.urls import include, path
from .routers import router

app_name = "files"

urlpatterns = [
    path("", include(router.urls)),
]
