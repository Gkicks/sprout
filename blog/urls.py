from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('blog/create_recipe/',
         views.CreateRecipe.as_view(), name='create_recipe'),
    path('blog/my_recipes/', views.user_recipes, name='user_recipes'),
    path('blog/edit_recipe/<slug>/',
         views.EditRecipe.as_view(), name='edit_recipe'),
    path('blog/confirm-delete/<slug>/',
         views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('<slug>/edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
    path('<slug>/delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
]
