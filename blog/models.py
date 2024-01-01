from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

CATEGORY = ((0, 'breakfast'), (1, 'starter'), (2, 'main'),
            (3, 'snack'), (4, 'side'), (5, 'dessert'), (6, 'drink'))


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_author')
    featured_image = CloudinaryField('image', default='placeholder')
    category = models.IntegerField(choices=CATEGORY, default=2)
    content = models.TextField(blank=True)
    ingregdients = models.TextField(blank=False)
    method = models.TextField(blank=False)
    servings = models.IntegerField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='recipe_like', blank=True)
    dislikes = models.ManyToManyField(
        User, related_name='recipe_dislike', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.recipe_name
