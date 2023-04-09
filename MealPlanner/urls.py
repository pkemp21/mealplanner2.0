from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('kitchen/', views.kitchen ),
    path('meal/', views.meal_page),
    path('plan/', views.plan_page)
]