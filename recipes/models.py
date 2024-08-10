from django.db import models


class Recipe(models.Model):

    user = model.ForeignKeny(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
