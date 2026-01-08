from models.user_preferences import UserPreferences
from logic.filter_recipes import filter_recipes

# mock preferences
prefs = UserPreferences(
    weekly_budget=60,
    diet_type="vegetarian",
    excluded_ingredients=["peanut"],
    calorie_target=2200,
    nutrition_goal="muscle_gain",
    activity_level="moderate",
    max_time_per_meal=30,
    cooking_skill_level="beginner",
    available_equipment=["stovetop"]
)

import json
from models.recipe import Recipe

# Load recipes from JSON
with open('data/recipes.json', 'r') as f:
    recipes_data = json.load(f)
    recipes = [Recipe.from_dict(d) for d in recipes_data]

filtered = filter_recipes(recipes, prefs)
print(filtered)
