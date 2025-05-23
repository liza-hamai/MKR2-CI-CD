from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile


class GalleryViewsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Nature")

        self.image = Image.objects.create(
            title="Mountain",
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            created_date=date.today(),
            age_limit=0
        )
        self.image.categories.add(self.category)

    def test_gallery_view_status_code_and_template(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')
        self.assertIn('categories', response.context)
        self.assertIn(self.category, response.context['categories'])

    def test_image_detail_view_status_code_and_template(self):
        response = self.client.get(reverse('image_detail', args=[self.image.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'image_detail.html')
        self.assertIn('image', response.context)
        self.assertEqual(response.context['image'], self.image)