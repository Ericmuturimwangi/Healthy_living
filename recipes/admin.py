from django.contrib import admin
from .models import Recipe

admin.site.register(Recipe)


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "meal_type",
        "calories",
        "instructions",
        "ingredients",
        "image",
    )
    list_filter = ("meal_type",)


# Register your models here.
