from django.urls import path
from .views import FoodListView

urlpatterns = [
    path('api/v1/foods/', FoodListView.as_view(), name='food-list'),
]
