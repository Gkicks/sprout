from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    # path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('blog/create_recipe/', views.CreateRecipe.as_view(), name='create_recipe'),
    # path('blog/add_recipe/', views.add_recipe, name='add_recipe'),
    path('blog/my_recipes/', views.user_recipes, name='user_recipes'),
    # path('<slug:slug>/edit_recipe/<int:recipe_id>',
    #      views.edit_recipe, name='edit_view')
]
