from pydantic import BaseModel
from typing import List, Dict

class Product(BaseModel):
    title: str
    description: str
    price: float
    stock: int
    images: List[str]
    category: str
    brand: str
    attributes: Dict
    tags: List[str]
    confidence: float
