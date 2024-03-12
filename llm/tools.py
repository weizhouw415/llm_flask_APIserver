from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import BaseTool
from typing import Any, Type

# Note that the docstrings here are crucial, as they will be passed along
# to the model along with the class name.
class Add(BaseModel):
    """Add two numbers together."""
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")
    
class Minus(BaseModel):
    """First number minus second number."""
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")

class Multiply(BaseModel):
    """Multiply two integers together."""
    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")

class Power(BaseModel):
    """An integer to the power of the second integer"""
    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")
