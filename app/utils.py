import os
import json

from .models.recipe import Recipe


def prepopulate_db(recipe_service):
    fixture_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "models",
            "fixtures",
            "data.json",
        )
    )
    with open(fixture_path) as f:
        dishes = json.loads(f.read())

        for dish in dishes:
            recipe_service.create_recipe(Recipe.from_dict(dish))