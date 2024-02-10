#!/usr/bin/python3
"""Defines an Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity that can be
    associated with a place or a location."""
    name = ""
