from django.shortcuts import render
from .models import Item

# Create your views here.


def get_todo_list(request):
    # get query set of all items from db
    items = Item.objects.all()
    # dictionary of all the items, passed to render below
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
