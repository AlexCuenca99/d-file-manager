from rest_framework import serializers

from .models import File


class FileModelSerializer(serializers.ModelSerializer):
    """
    Serializer for the File model.
    """

    file_name = serializers.CharField(read_only=True, source="get_file_name")

    class Meta:
        model = File
        fields = "__all__"
