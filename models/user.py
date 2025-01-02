#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablname__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    """DBStorage relationship"""
    places = relationship(
        "Place",
        backref="user",
        cascade="all, delete, delete-orphan"
    )

    """DBStorage relationship"""
    reviews = relationship(
        "Review",
        backref="user",
        cascade="all, delete, delete-orphan"
    )
