from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Maps(db.Model):
    __tablename__ = 'distance' 

    id = db.Column(db.Integer, primary_key=True)
    _location1 = db.Column(db.String(255), unique=True, nullable=False)
    _location2 = db.Column(db.String(255), unique=False, nullable=False)
    
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, depart, arrive):

        self._location2 = arrive   # variables with self prefix become part of the object, 
        self._location1 = depart

    @property
    def arrive(self):
        return self._location2
    
    @arrive.setter
    def arrive(self, arrive):
        self._location2 = arrive

    

    @property
    def depart(self):
        return self._location1
    
    @depart.setter
    def depart(self, depart):
        self._location1 = depart

    def __str__(self):
        return json.dumps(self.read())

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
            "id": self.id,
            "arrive": self.arrive,
            "depart": self.depart,
            
        }

    # CRUD update: updates user arrive, knew, phone
    # returns self
    def update(self, arrive="", depart=""):
        """only updates values with length"""
        if len(arrive) > 0:
            self.arrive = arrive
        if len(depart) > 0:
            self.depart = depart
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
"""CRUD DONE"""

def initFacts():

    """Builds sample user/note(s) data"""
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        u1 = Maps( arrive='FCO', depart='LAX', )
        u2 = Maps( arrive='CDG', depart='JFK', )
        u3 = Maps( arrive='SEA', depart='LHR', )
        u4 = Maps( arrive='SIN', depart='DXB', )
        u5 = Maps( arrive='ATL', depart='SFO', )

        maps = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for map in maps:
            try:
                '''add a few 1 to 4 notes per user'''
                fact.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error:")