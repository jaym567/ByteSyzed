from dataclasses import dataclass
from typing import List, Optional

@dataclass
class UserPreferences:
    weekly_budget: float
    diet_type: str
    excluded_ingredients: List[str]
    calorie_target: int
    nutrition_goal: str
    activity_level: str
    max_time_per_meal: int
    cooking_skill_level: str
    available_equipment: List[str]
