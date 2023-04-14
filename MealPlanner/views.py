from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from .models import *
from .functions import *

# Create your views here.
def landing_page(request):

    meals = []
    if Meals.objects.all():
        for x in Meals.objects.all():
            meals.append(x)
    else:
        meals = ['test']

    context = {
        'meals':meals
    }

    return render(request, 'index.html', context)
    #Display meal optinos
    #Allow to add meal (Hello fresh or Blue apron)
    #Link to kitchem, meals, shopping list

def kitchen(request):
    return render(request, 'kitchen.html')
    #list and Edit what is in the kitchen
    #Show what is missing based on plan

def meal_page(request):
    return render(request, 'meal.html')
    #Display meal specific info
    #Show what ingredients are in kitchen or not
    #

def plan_page(request):
    return render(request, 'plan.html')

def add_meal(request):

    if request.method == "POST":
        try:
            #Add meal to DB
            mealData = get_meal(request.POST['url'])
            meal = Meals.objects.create(
                title   = mealData['title'], 
                imageUrl  = mealData['imgUrl'],
                mealUrl =  mealData['mealUrl']
                )
            meal.save()

            #Add ingredients to DB
            for x in mealData['ingredients']:
                temp = x[0].split()
                ingredients = Ingredients.objects.create(
                    amount = temp[0],
                    measurement = temp[1],
                    ingredient = x[1],
                    meal = meal
                )
                ingredients.save()

            #Add tags to DB
            for x in mealData['tags']:
                tag = Tags.objects.create(
                    tag = x,
                    meal = meal
                )
                tag.save()
        except(IntegrityError):
            return render(redirect, landing_page)
            
    return render(redirect, landing_page)