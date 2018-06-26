from django.test import TestCase
from .models import Bucketlist
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
