from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        # create a test item with just name
        item = Item.objects.create(name='Test item')
        # done status of the item should be false, as it was not set
        self.assertFalse(item.done)
