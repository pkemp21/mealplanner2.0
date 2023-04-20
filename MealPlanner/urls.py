from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('kitchen/', views.kitchen ),
    path('plan/', views.plan_page, name = 'plan'),
    path('add/', views.add_meal, name = 'add'),
    path('shopping/', views.shopping, name = 'shopping'),
    path('details/<str:mealName>/', views.meal_page, name = 'meal'),
    path('plan_add/<str:mealName>/', views.add_meal_to_plan, name = 'addToPlan'),
    path('delete/<str:mealName>/', views.delete, name = 'delete'),
]