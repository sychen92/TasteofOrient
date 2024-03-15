from django.contrib import admin
from .models import Recipe, UserPreference  # Make sure to use your actual model names

admin.site.register(Recipe)
admin.site.register(UserPreference)
