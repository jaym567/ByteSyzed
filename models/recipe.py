from dataclasses import dataclass
from typing import List, Dict, Any

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
    def from_dict(cls, data: Dict[str, Any]) -> 'Recipe':
        return cls(
            id=data.get("id", ""),
            name=data.get("name", "Unknown"),
            ingredients=data.get("ingredients", []),
            calories=data.get("calories", 0),
            price=data.get("price", 0.0),
            prep_time=data.get("prep_time", 0),
            dietary_tags=data.get("dietary_tags", []),
            equipment=data.get("equipment", []),
            difficulty=data.get("difficulty", "medium")
        )