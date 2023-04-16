from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('kitchen/', views.kitchen ),
    path('<str:mealName>/', views.meal_page, name = 'meal'),
    path('plan/', views.plan_page),
    path('add/', views.add_meal, name = 'add')
]