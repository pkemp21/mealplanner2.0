from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Meals(models.Model):
    title            = models.CharField(max_length=120, unique=True)
    imageUrl         = models.URLField(null=True)
    # same_ingredients = models.IntegerField(default=0)
    # dishType         = models.CharField(max_length=64, null=True)
    # servingSize      = models.CharField(max_length=64, null=True)
    mealUrl          = models.URLField(null=True)

    def __str__(self):
        return self.title

class Ingredients(models.Model):
    amount      = models.CharField(max_length=64)
    measurement = models.CharField(max_length=64, default='count')
    ingredient  = models.CharField(max_length=64)
    meal        = models.ForeignKey(Meals, on_delete=models.CASCADE)

    def __str__(self):
        return self.ingredient
    
    class Meta:
        ordering=['amount']

class Tags(models.Model):
    tag  = models.CharField(max_length=64)
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

class Plan(models.Model):
    meal = ForeignKey(Meals, on_delete=CASCADE, unique=True)
    

    def __str__(self):
        return str(self.meal)


class Kitchen(models.Model):
    item = models.CharField(max_length=64)

    def __str__(self):
        return str(self.item)