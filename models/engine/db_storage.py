from os import getenv
from sqlalchemy import create_engine
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ engine DBStorage"""

    __engine = None
    __session = None
    cls_dict = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def __init__(self):
        """Instantiation of DBStorage class
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                      .format(getenv(HBNB_MYSQL_USER),
                                              getenv(HBNB_MYSQL_PWD),
                                              getenv(HBNB_MYSQL_DB)),
                                      pool_pre_ping=True)
        if getenv(HBNB_ENV) == "test":
            Base.metadata.drop_all(bind=engine)

    def all(self, cls=None):
        """query on the current database session
        """
        d = {}
        if cls:
            obj = self.__session.query(cls)
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            d[key] = obj
        else:
            for obj in self.__session.query(cls_dict.values()):
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                d[key] = obj
        return d

    def new(self, obj):
        """add the object to the current database session (self.__session)
        """
        self.__session.add(obj)
        self.save()

    def save(self):
        """commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reate all tables in the database and
        create the current database session
        """
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
