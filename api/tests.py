from xml.dom import ValidationErr
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import AIModel
from django.core.files.uploadedfile import SimpleUploadedFile
import json

class BasicAIAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_returns_empty_list(self):
        url = reverse('model-list')  # Use the named URL pattern
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data, [])

class AIModelErrorHandlingTestCase(TestCase):
    def test_invalid_model_creation(self):
        with self.assertRaises(ValueError):
            AIModel.objects.create(name='', description='Test Description')
    
    # Add more error handling tests as needed...
