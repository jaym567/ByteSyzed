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
from logic.load_recipes import load_recipes_from_json

recipes = load_recipes_from_json("data/recipes.json")
filtered = filter_recipes(recipes, prefs)

print(filtered)

