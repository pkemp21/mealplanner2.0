from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from .models import *
from .functions import *

# Create your views here.
def landing_page(request):

    meals = []
    plan  = []

    if Plan.objects.all():
        for x in Plan.objects.all():
            plan.append(x.meal)

    if Meals.objects.all():
        for x in Meals.objects.all():
            if x not in plan:
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
        "meal"        : Meals.objects.get(title=mealName),
        'ingredients' : Ingredients.objects.filter(meal=meal.id),
        'tags'        : Tags.objects.filter(meal=meal.id),
    }

    return render(request, 'meal.html', context)
    #Display meal specific info
    #Show what ingredients are in kitchen or not
    #

def plan_page(request):

    meals = []
    for x in Plan.objects.all():
        meals.append(x)

    context = {
        'meals' : meals,
    }

    return render(request, 'plan.html', context)

def add_meal(request):

    if request.method == "POST":
            #Add meal to DB
            mealData = get_meal(request.POST['url'])
            if not mealData['ingredients']:
                return redirect(landing_page)

            
            try:
                meal = Meals.objects.create(
                    title     = mealData['title'], 
                    imageUrl  = mealData['imgUrl'],
                    mealUrl   = mealData['mealUrl']
                    )
                meal.save()
            except IntegrityError:
                return redirect(landing_page)

            #Add ingredients to DB
            for x in mealData['ingredients']:
                if x[0] == '':
                    x[0] = '1 unit'
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
            
    return redirect(landing_page)

def add_meal_to_plan(request, mealName):

    mealX = Meals.objects.get(title=mealName)

    if Plan.objects.filter(meal=mealX).exists():
        return(redirect(plan_page))
    try:
        plan = Plan.objects.create(
            meal = mealX
        )
        plan.save()
        return redirect(plan_page)
    except(IntegrityError):
        return redirect(plan_page)
    
def delete(request, mealName):

    mealX = Meals.objects.get(title=mealName)


    Plan.objects.filter(meal = mealX).delete()
    
    return redirect(plan_page)

def shopping(request):

    mealsInPlan = Plan.objects.all()
    planIngredients = []

    if mealsInPlan:
        for x in mealsInPlan:
            # planMeal = Meals.objects.get(title = x)
            ingredients = Ingredients.objects.filter(meal=Meals.objects.get(title = x))
            for x in ingredients:
               planIngredients.append([x.amount, x.measurement, x.ingredient])
    
    consolidatedIngredients = normalize_units(planIngredients)

    # else:
    #     planIngredients = []
    context = {
        'ingredients' : consolidatedIngredients
    }

    return render(request, 'shopping.html', context)