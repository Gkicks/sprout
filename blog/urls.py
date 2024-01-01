from . import views
from django.urls import path
# from .views import HomePageView

# app_name = 'blog'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]
