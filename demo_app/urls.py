# type: ignore
from django.urls import path
from . import views
from .views import FoodDetail,CreateItem

app_name = 'demo_app'

urlpatterns = [
    path('',views.my_view),
    path('home/',views.food, name = 'food'),
    path('<int:pk>/',FoodDetail.as_view(),name = 'food_detail'),
    path('add/',CreateItem.as_view(),name = 'add_item'),
    path('update/<int:id>/',views.update_item,name = 'update_item'),
    path('delete/<int:id>/',views.delete_item,name = 'delete_item'),
]