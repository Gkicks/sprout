from . import views
from django.urls import path
# from .views import HomePageView

# app_name = 'blog'

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
]
