""" database dependencies to support sqliteDB examples """

import json
from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class FdPost(db.Model):
    __tablename__ = 'fdposts'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _title = db.Column(db.String(255), unique=True, nullable=False)
    _text = db.Column(db.String(255), unique=False, nullable=False)
    _imageURL = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, title, text, imageURL):
        self._title = title    # variables with self prefix become part of the object, 
        self._text = text
        self._imageURL = imageURL

    # a name getter method, extracts name from object
    @property
    def title(self):
        return self._title
    
    # a setter function, allows name to be updated after initial object creation
    @title.setter
    def title(self, title):
        self._title = title
    
    # a getter method, extracts email from object
    @property
    def text(self):
        return self._text
    
    # a setter function, allows name to be updated after initial object creation
    @text.setter
    def uid(self, text):
        self._text = text
    
    # a getter method, extracts email from object
    @property
    def imageURL(self):
        return self._imageURL
    
    # a setter function, allows name to be updated after initial object creation
    @imageURL.setter
    def uid(self, imageURL):
        self._text = imageURL

    
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
            "title": self.title,
            "text": self.text,
            "imageURL": self.imageURL
        }
    

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, title="", text="", imageURL=""):
        """only updates values with length"""
        if len(title) > 0:
            self.title = title
        if len(text) > 0:
            self.text = text
        if len(imageURL) > 0:
            self.imageURL = imageURL
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
def initUsers():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
        """Tester data for table"""
        u1 = FdPost(title="New York City", text="Fortnite", imageURL="amomh.com")
        u2 = FdPost(title="San Diego", text="Among", imageURL="fort.com")

        users = [u1, u2]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.uid}")
            