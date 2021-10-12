from django.shortcuts import render, redirect
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


def add_item(request):
    # if POST request, means it is Add New Item form
    if request.method == 'POST':
        # two new variables to hold info from form
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        # create new db record using info in variables above
        Item.objects.create(name=name, done=done)
        # redirect user to home page
        return redirect('get_todo_list')
    # if not a POST request, then just get the page and render it
    return render(request, 'todo/add_item.html')
