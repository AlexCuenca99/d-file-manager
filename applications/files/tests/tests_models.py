from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import File
from ..utils import set_file_path

User = get_user_model()


class FileTest(TestCase):
    """Test module for File model"""

    def setUp(self) -> None:
        self.file_info = self.generate_file_info()
        self.file = self.generate_file()
        self.user_info = self.generate_user_info()

    def generate_file(self) -> None:
        """Generate a simple file"""
        file = SimpleUploadedFile("test_file.txt", b"dummy content")
        return file

    def generate_file_info(self) -> dict:
        """Generate a file info dict"""
        return {"file": self.generate_file(), "owner": 1}

    def generate_user_info(self) -> dict:
        """Generate a user info dict"""
        return {
            "email": "lakiboj883@royalka.com",
            "birth": "1999-12-02",
            "first_name": "Alex",
            "last_name": "Cuenca",
            "phone": "0989181061",
            "gender": "FEM",
            "username": "AlexAgent",
            "password": "randompassword123",
        }

    def test_file_creation(self) -> None:
        """Test file creation"""

        # Create a user
        user = User.objects.create_user(**self.user_info)
        self.file_info["owner"] = user

        # Crate a File object
        file = File.objects.create(**self.file_info)
        # self.assertEqual(
        #     file.file.name, set_file_path(file, self.file_info["file"].name)
        # )
        self.assertEqual(File.objects.all().count(), 1)
