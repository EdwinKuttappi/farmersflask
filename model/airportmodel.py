""" database dependencies to support sqliteDB examples """
import os
import json
from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class AirportPost(db.Model):
    __tablename__ = 'airportposts'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _city = db.Column(db.String(255), unique=True, nullable=False)
    _airport = db.Column(db.String(255), unique=False, nullable=False)
    
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, city, airport):
        self._city = city    # variables with self prefix become part of the object, 
        self._airport = airport

    # a name getter method, extracts name from object
    @property
    def city(self):
        return self._city
    
    # a setter function, allows name to be updated after initial object creation
    @city.setter
    def city(self, city):
        self._city = city
    
    # a getter method, extracts email from object
    @property
    def airport(self):
        return self._airport
    
    # a setter function, allows name to be updated after initial object creation
    @airport.setter
    def uid(self, airport):
        self._airport = airport
    
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
            "city": self.city,
            "airport": self.airport
        }
    

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, city="", airport=""):
        """only updates values with length"""
        if len(city) > 0:
            self.city = city
        if len(airport) > 0:
            self.airport = airport
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
def initAirports():
    with app.app_context():
        """Create database and tables"""
        
        db.create_all()
        """Tester data for table"""
        u1 = AirportPost(city="Paris", airport="Paris-Le Bourget")
        u2 = AirportPost(city="Berlin", airport="Berlin-Tegel")

        users = [u1, u2]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.uid}")