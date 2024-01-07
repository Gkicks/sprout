from . import views
from django.urls import path
# from .views import HomePageView

# app_name = 'blog'

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('blog/add_recipe/', views.add_recipe, name='add_recipe'),
]
