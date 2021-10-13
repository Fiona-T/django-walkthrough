from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        # instansiate form without name field to simulate user
        # completing form without filling in name field
        form = ItemForm({'name': ''})
        # form should not be valid
        self.assertFalse(form.is_valid())
        # check if name key is in the dictionary returned of form errors
        self.assertIn('name', form.errors.keys())
        # check if first item in list of errors returned on name field
        # is the below string - field is required
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # instansiate form with just name field
        form = ItemForm({'name': "Test todo item"})
        # form should be valid
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # instansiate empty form
        form = ItemForm()
        # form Meta fields attribute should be equal to below list
        # i.e. the explicitly defined fields in the Meta innerclass
        self.assertEqual(form.Meta.fields, ['name', 'done'])
