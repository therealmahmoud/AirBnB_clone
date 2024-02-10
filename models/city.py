#!/usr/bin/python3
"""Defines a City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city associated with a state."""
    state_id = ""
    name = ""
