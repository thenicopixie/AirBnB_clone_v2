#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
import models
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review',
                           cascade='all, delete',
                           backref='place')
    amenities = relationship("Amenity",
                             secondary=place_amenity,
                             viewonly=False,
                             backref='place')

    @property
    def reviews(self):
        """ returns the list of Review instances with place_id
        equals to the current Place.id
        """
        return [value for value in models.storage.all(Review).values()
                if value.place_id == self.id]

    if getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def amenities(self):
            """returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            print("getter")
            return [value
                    for value in models.storage.all(models.Amenity).values()
                    if value.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """handles append method for adding an Amenity.id to
            the attribute amenity_ids
            """
            if isinstance(obj, models.Amenity):
                if self.id in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
