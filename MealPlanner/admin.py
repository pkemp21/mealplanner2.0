from django.contrib import admin

# Register your models here.
from .models import Meals, Ingredients, Tags

admin.site.register(Meals)
admin.site.register(Ingredients)
admin.site.register(Tags)
