from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):

    def test_get_todo_list(self):
        # using built in HTTP client to get the url
        response = self.client.get('/')
        # check the response code is 200 i.e. successful
        self.assertEqual(response.status_code, 200)
        # check that correct template was used
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item(self):
        # using built in HTTP client to get the url
        response = self.client.get('/add')
        # check the response code is 200 i.e. successful
        self.assertEqual(response.status_code, 200)
        # check that correct template was used
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item(self):
        # create a test item
        item = Item.objects.create(name='Test todo item')
        # using built in HTTP client to get the url - with item id
        response = self.client.get(f'/edit/{item.id}')
        # check the response code is 200 i.e. successful
        self.assertEqual(response.status_code, 200)
        # check that correct template was used
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # client POST on the add url, with name as if we added an item
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # check the redirect goes to correct url
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # create a test item
        item = Item.objects.create(name='Test todo item')
        # using built in HTTP client to get the url - with item id
        response = self.client.get(f'/delete/{item.id}')
        # check the redirect goes to correct url
        self.assertRedirects(response, '/')
        # check the item was deleted - get from db using this item id,
        existing_items = Item.objects.filter(id=item.id)
        # length should now be zero since the item was deleted
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # create a test item
        item = Item.objects.create(name='Test todo item', done=True)
        # using built in HTTP client to get the url - with item id
        response = self.client.get(f'/toggle/{item.id}')
        # check the redirect goes to correct url
        self.assertRedirects(response, '/')
        # cget from db using this item id,
        updated_item = Item.objects.get(id=item.id)
        # done status of item should now be false
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        # create a test item
        item = Item.objects.create(name='Test todo item')
        # call post on the edit view, editing the name of above item
        response = self.client.post(
            f'/edit/{item.id}', {'name': 'Updated name'})
        # check the redirect goes to correct url
        self.assertRedirects(response, '/')
        # get from db using this item id,
        updated_item = Item.objects.get(id=item.id)
        # name of item should match the updated name
        self.assertEqual(updated_item.name, 'Updated name')
