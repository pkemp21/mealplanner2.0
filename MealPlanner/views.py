from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'index.html', {'name': 'Phil'})
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