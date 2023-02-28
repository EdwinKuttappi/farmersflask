""" database dependencies to support sqliteDB examples """
import os
import json
from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class MapsPost(db.Model):
    __tablename__ = 'mapspost'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _location1 = db.Column(db.String(255), unique=True, nullable=False) # _city
    _location2 = db.Column(db.String(255), unique=False, nullable=False) # _airport
    
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, location1, location2):
        self._location1 = location1 # _city
        self._location2 = location2 # _airport

    # a name getter method, extracts name from object
    @property
    def city(self):
        return self._location1
    
    # a setter function, allows name to be updated after initial object creation
    @city.setter
    def city(self, location1):
        self._location1 = location1
    
    # a getter method, extracts email from object
    @property
    def airport(self):
        return self._location2
    
    # a setter function, allows name to be updated after initial object creation
    @airport.setter
    def uid(self, location2):
        self._location2 = location2
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "location1": self.location1,
            "location2": self.location2
        }
    

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, location1="", location2=""):
        """only updates values with length"""
        if len(location1) > 0:
            self.location1 = location1
        if len(location2) > 0:
            self.location2 = location2
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# Builds working data for testing
def initMaps():
    with app.app_context():
        """Create database and tables"""
        
        db.create_all()
        """Tester data for table"""
        u1 = MapsPost(location1="Paris", location2="Paris-Le Bourget")
        u2 = MapsPost(location1="Berlin", location2="Berlin-Tegel")

        users = [u1, u2]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.uid}")