from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        # create a test item with just name
        item = Item.objects.create(name='Test item')
        # done status of the item should be false, as it was not set
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        # create test item to test the name returned with string method
        item = Item.objects.create(name='Test todo item')
        # check the item name is returned when item rendered as a string
        self.assertEqual(str(item), 'Test todo item')
