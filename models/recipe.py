from dataclasses import dataclass
from typing import List, Dict, Any


class RecipeValidationError(Exception):
    def __init__(self, message: str, recipe_id: str | None = None):
        self.recipe_id = recipe_id
        super().__init__(message)

@dataclass
class Recipe:
    id: str
    name: str
    ingredients: List[str]
    calories: int
    price: float
    prep_time: int
    dietary_tags: List[str]
    equipment: List[str]
    difficulty: str
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Recipe":
        recipe_id = data.get("id", "unknown")

        required_fields = ["id", "name", "ingredients", "calories", "price", "prep_time"]
        for field in required_fields:
            if field not in data:
                raise RecipeValidationError(
                    f"Missing required field: {field}",
                    recipe_id=recipe_id
                )

        if not isinstance(data["ingredients"], list) or len(data["ingredients"]) == 0:
            raise RecipeValidationError(
                "Recipe must have at least one ingredient",
                recipe_id=recipe_id
            )

        if not isinstance(data["calories"], int) or data["calories"] < 0:
            raise RecipeValidationError(
                "Calories must be a non-negative integer",
                recipe_id=recipe_id
            )

        if not isinstance(data["price"], (int, float)) or data["price"] < 0:
            raise RecipeValidationError(
                "Price must be a non-negative number",
                recipe_id=recipe_id
            )

        if not isinstance(data["prep_time"], int) or data["prep_time"] < 0:
            raise RecipeValidationError(
                "Prep time must be a non-negative integer",
                recipe_id=recipe_id
            )

        return cls(
            id=str(data["id"]),
            name=str(data["name"]),
            ingredients=list(data["ingredients"]),
            calories=data["calories"],
            price=float(data["price"]),
            prep_time=data["prep_time"],
            dietary_tags=list(data.get("dietary_tags", [])),
            equipment=list(data.get("equipment", [])),
            difficulty=str(data.get("difficulty", "medium"))
        )

