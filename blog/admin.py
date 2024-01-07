from django.contrib import admin
from .models import Recipe, Comment


class RecipeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Recipe)
admin.site.register(Comment)
