from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile


class GalleryViewsTestCase(TestCase):
    def setUp(self):
        # Тестова категорія
        self.category = Category.objects.create(name="Nature")

        # Фейкове зображення
        self.image = Image.objects.create(
            category=self.category,
            title="Mountain",
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )