from enum import Enum
from pydantic import BaseModel, Field


class Category(Enum):
    """Category of an item"""

    TOOLS = "tools"
    CONSUMABLES = "consumables"


class Item(BaseModel):
    """Representation of an item in the system."""

    name: str = Field(description="Name of the item.")
    price: float = Field(description="Price of the item in Euro.")
    count: int = Field(description="Amount of instances of this item in stock.")
    id: int = Field(description="Unique integer that specifies this item.")
    category: Category = Field(description="Category this item belongs to.")
