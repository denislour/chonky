from typing import List, Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class Base(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.now())
    modified_at: datetime = Field(default=datetime.now())


class User(Base, table=True):
    username: str = Field(max_length=200)
    full_name: str = Field(max_length=50)
    password: str = Field(max_length=128)
    password: str = Field(max_length=128)
    password: str = Field(max_length=128)

    # Relation fields
    notes: List["Note"] = Relationship(back_populates="user")


class Note(Base, table=True):
    title: str = Field(max_length=255)
    content: str = Field()

    # Relation fields
    user_id: int = Field(default=None, foreign_key="user.id")
    author: Optional[User] = Relationship(back_populates="notes")
