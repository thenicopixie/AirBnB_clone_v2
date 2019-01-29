#!/usr/bin/python3
"""DBStorage engine"""
from os import getenv
from sqlalchemy import create_engine
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """ DBStorage class
    Attributes:
        __engine:  an instance of Engine
        __session: Session objects which are bound to our database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage class
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name(cls) or query all
        types of objects (User, State, City, Amenity, Place and Review)
        if cls is None.
            Return:
               return a dictionary
        """
        d = {}
        cls_list = [State, City, User, Place, Review, Amenity]
        if cls:
            for obj in self.__session.query(eval(cls)).all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                d[key] = obj
        else:
            for item in cls_list:
                for obj in self.__session.query(item):
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    d[key] = obj
        return d

    def new(self, obj):
        """add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """calls remove method on the private session attribute"""
        self.__session.remove()
