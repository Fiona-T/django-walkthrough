from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # display the name of each item in admin panel instead of Item object
    # overrides the default __str__ method from Django base Model class
    def __str__(self):
        return self.name
