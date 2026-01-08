import json
from typing import List
from models.recipe import Recipe


def load_recipes_from_json(path: str) -> List[Recipe]:
    valid_recipes = []

    with open(path, "r") as f:
        data = json.load(f)

    for idx, recipe_dict in enumerate(data):
        try:
            recipe = Recipe.from_dict(recipe_dict)
            valid_recipes.append(recipe)
        except ValueError as e:
            recipe_id = recipe_dict.get("id", f"index {idx}")
            print(f"[WARN] Skipping recipe {recipe_id}: {e}")

    print(f"[INFO] Loaded {len(valid_recipes)} valid recipes")

    return valid_recipes
