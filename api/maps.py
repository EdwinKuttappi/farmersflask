from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.maps import Maps

maps_api = Blueprint('maps_api', __name__,
                   url_prefix='/api/maps')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
mapsapi = Api(maps_api)

class FdPostAPI(Resource):        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            title = body.get('title')
            if title is None or len(title) < 2 or len(title) > 30:
                return {'message': f'Name is missing, or is less than 2 characters, or is more than 30 characters'}, 210
            # validate uid
            text = body.get('text')
            if text is None or len(text) < 2 or len(text) > 800:
                return {'message': f'Text is missing, or is less than 2 characters, or is more than 800 characters'}, 210
            
            imageURL = body.get('imageURL')
            if imageURL is None:
                return {'message': f'imageURL is missing'}, 210
            # look for password and dob
         

            ''' #1: Key code block, setup USER OBJECT '''
            uo = mapsPost(title=title, text=text, imageURL=imageURL)
            
            ''' Additional garbage error checking '''

            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {title}, format error'}, 210

    class _Read(Resource):
        def get(self):
            users = FdPost.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    # comment
    # building RESTapi endpoint
    api.add_resource(_Create, '/post')
    api.add_resource(_Read, '/')
