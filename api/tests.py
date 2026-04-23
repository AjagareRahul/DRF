from django.test import TestCase
from .models import Products


class HomePageTests(TestCase):
    def test_homepage_loads(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Product Catalog')


class ProductApiTests(TestCase):
    def test_products_api_returns_data(self):
        Products.objects.create(name='Phone', price=29999)

        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'id': 1, 'name': 'Phone', 'price': 29999}])
