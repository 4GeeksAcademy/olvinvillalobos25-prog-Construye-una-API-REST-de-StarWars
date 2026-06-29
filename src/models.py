from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(
        String(80),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(80),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean(),
        nullable=False,
        default=True
    )

    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="user"
    )

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }


class Character(db.Model):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    gender: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    height: Mapped[str] = mapped_column(
        String(20),
        nullable=True
    )

    eye_color: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="character"
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "eye_color": self.eye_color
        }


class Planet(db.Model):
    __tablename__ = "planet"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(120),
        nullable=False
    )

    climate: Mapped[str] = mapped_column(
        String(80),
        nullable=True
    )

    terrain: Mapped[str] = mapped_column(
        String(80),
        nullable=True
    )

    population: Mapped[str] = mapped_column(
        String(50),
        nullable=True
    )

    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="planet"
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population
        }


class Favorite(db.Model):
    __tablename__ = "favorite"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False
    )

    character_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("character.id"),
        nullable=True
    )

    planet_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("planet.id"),
        nullable=True
    )

    user: Mapped["User"] = relationship(
        back_populates="favorites"
    )

    character: Mapped[Optional["Character"]] = relationship(
        back_populates="favorites"
    )

    planet: Mapped[Optional["Planet"]] = relationship(
        back_populates="favorites"
    )

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }
