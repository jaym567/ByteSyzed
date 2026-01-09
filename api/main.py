from fastapi import FastAPI, HTTPException
from api.schemas import UserPreferencesSchema, RecipeResponseSchema
from logic.loader import load_recipes_from_json
from logic.filter import filter_recipes
from logic.errors import RecipeValidationError

app = FastAPI(title="ByteSyzed API")

# Load once at startup
try:
    RECIPES = load_recipes_from_json("data/recipes.json")
except RecipeValidationError as e:
    raise RuntimeError(f"Failed to load recipes: {e}")

@app.post("/recipes/filter", response_model=list[RecipeResponseSchema])
def filter_recipes_endpoint(prefs: UserPreferencesSchema):
    try:
        results = filter_recipes(RECIPES, prefs)
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
