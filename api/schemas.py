from pydantic import BaseModel
from typing import List, Optional

class UserPreferencesSchema(BaseModel):
    budget: Optional[float] = None
    dietary_restrictions: Optional[List[str]] = None
    max_calories: Optional[int] = None
    equipment: Optional[List[str]] = None

class RecipeResponseSchema(BaseModel):
    id: str
    name: str
    calories: int
    price: float
    prep_time: int
    dietary_tags: List[str]
