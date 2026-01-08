from typing import List
from models.recipe import Recipe
from models.user_preferences import UserPreferences

def filter_recipes(recipes: List[Recipe], prefs: UserPreferences) -> List[Recipe]:
    """
    Filters recipes based on user preferences.
    """
    filtered_recipes = []
    
    for recipe in recipes:
        # 1. Budget check (simplified: naive check against weekly budget / 21 meals? 
        #    Actual logic might differ, for now just pass checks)
        
        # 2. Diet type
        if prefs.diet_type and prefs.diet_type not in recipe.dietary_tags:
            # logic might be complex e.g. "vegetarian" implies no meat. 
            # For now, if diet_type is strictly required as a tag:
            continue 
            
        # 3. Excluded ingredients
        if any(excl.lower() in ing.lower() for ing in recipe.ingredients for excl in prefs.excluded_ingredients):
            continue
            
        # 4. Filter by Time
        if recipe.prep_time > prefs.max_time_per_meal:
            continue
            
        filtered_recipes.append(recipe)
        
    return filtered_recipes
