from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('kitchen/', views.kitchen ),
    path('plan/', views.plan_page, name = 'plan'),
    path('add/', views.add_meal, name = 'add'),
    path('details/<str:mealName>/', views.meal_page, name = 'meal'),
    path('plan_add/', views.add_meal_to_plan, name = 'addToPlan'),
]