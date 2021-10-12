from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

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
        # instance of form with data in POST request
        form = ItemForm(request.POST)
        # call is_valid method on the form - Django compares data
        # in form with data required on the model
        if form.is_valid():
            form.save()
            # redirect user to home page
            return redirect('get_todo_list')
    # if not a POST request, then just get the page and render it
    # create instance of form class (from forms.py) to render form
    form = ItemForm()
    # context contains the empty form, passing this to render below
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
