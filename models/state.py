#!/usr/bin/python3
"""
Defines the State class that inherits from BaseModel.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
