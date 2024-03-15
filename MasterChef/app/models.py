from django.db import models
from django.contrib.auth.models import User

# Define a model for the recipes
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    external_url = models.URLField()  # URL to the external recipe
    youtube_url = models.URLField(blank=True, null=True)  # URL to the corresponding YouTube video
    # Add other fields as necessary

# Define a model for user preferences
class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)
    # Add other fields as necessary

