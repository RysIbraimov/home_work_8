from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
