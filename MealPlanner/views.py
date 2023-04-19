from sqlite3 import IntegrityError
from turtle import title
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
        meals = ['No Meals found. Add some!']

    context = {
        'meals':meals
    }

    return render(request, 'index.html', context)
    #Display meal options
    #Allow to add meal (Hello fresh or Blue apron)
    #Link to kitchem, meals, shopping list

def kitchen(request):
    return render(request, 'kitchen.html')
    #list and Edit what is in the kitchen
    #Show what is missing based on plan

def meal_page(request, mealName):

    meal = Meals.objects.get(title=mealName)
    context = {
        "meals"       : Meals.objects.filter(title=mealName),
        'ingredients' : Ingredients.objects.filter(meal=meal.id),
        'tags'        : Tags.objects.filter(meal=meal.id),
    }

    return render(request, 'meal.html', context)
    #Display meal specific info
    #Show what ingredients are in kitchen or not
    #

def plan_page(request):

    meals = []
    if Plan.objects.all():
        for x in Plan.objects.all():
            meals.append(x)
    else:
        meals = ['No Meals found. Add some!']

    context = {
        'meals'       : meals,
        # 'ingredients' : ingredients,
    }

    return render(request, 'plan.html', context)

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
                if len(temp) == 2:
                    amount = temp[0]
                    measurement = temp[1]
                else:
                    amount = 1
                    measurement = temp[0]
                ingredients = Ingredients.objects.create(
                    amount = amount,
                    measurement = measurement,
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
            return redirect(landing_page)
            
    return redirect(landing_page)

def add_meal_to_plan(request, mealName):

    # meal = Meals.objects.get(title=mealName)

    # currentPlan = Plan.objects.get(all)

    # if meal not in currentPlan:
    #     plan = Plan.objects.create(
    #         meal = meal
    #     )

    #     plan.save()
    
    
    return redirect(landing_page)