from django.contrib import admin
from .models import Recipe, Comment, Rating


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['recipe_name', 'author', 'created_on', 'approved']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'recipe', 'created_on', 'approved']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['rating', 'recipe']
