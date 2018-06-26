from django.test import TestCase
from .models import Bucketlist
from rest_framework import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
# Create your tests here.
class ModelTestCase(TestCase):
    ''' defines the test suite for bucket checklist'''

    def setUp(self):
        """ define the test client for test var """
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)
# define view case
class ViewTestCase(TestCase):
    """ test suite for api views """

    def setUp(self):
        """ define the test client and other test variables."""
         self.client = APIClient()
         self.bucketlist_data = {'name': 'Go to Ibiza'}
         self.response = self.client.post(
         reverse('create'),
         self.bucketlist_data,
         format="json"
         )
    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability"""
        
