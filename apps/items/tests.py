from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from apps.items.models import Item
from apps.items.serializers import ItemSerializer

class ItemsTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_existing_item(self):
        """
        Test retrieving existing item from the db
        """
        item = Item.objects.create(
            name='Item A', 
            price=2000, 
            description='description text'
        )
        response = self.client.get(f'/items/{item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"], ItemSerializer(item).data)

    def test_retrieve_without_item_id(self):
        """
        Test retrieving item without passing the item_id path variable
        """
       
        response = self.client.get(f'/items/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_retrieve_nonexistent_item(self):
        """
        Test retrieving nonexistent item
        """
        response = self.client.get('/items/99/')  # Assuming item with id 99 does not exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_item(self):
        """
        Test creating valid item
        """
        data = {'name': 'Item A', 'price': 2000, 'description': 'description text'}
        response = self.client.post('/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.all().count(), 1)

    def test_create_invalid_item(self):
        """
        Test creating invalid item
        """
        data = {'name': 'New Item', 'description': 'description text'}  # Missing 'price'
        response = self.client.post('/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Item.objects.count(), 0)  # No item