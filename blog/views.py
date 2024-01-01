from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.


class HomePageView(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "blog/index.html"
    paginate_by = 4
