from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.mapsmodel import MapsPost

maps_api = Blueprint('maps_api', __name__,
                   url_prefix='/api/maps')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(maps_api)

class MapsPostAPI(Resource):        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            location1 = body.get('location1')
            location2 = body.get('location2')

            ''' #1: Key code block, setup USER OBJECT '''
            uo = MapsPost(location1=location1, location2=location2)

            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {location1}, format error'}, 210

    class _Read(Resource):
        def get(self):
            users = MapsPost.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    # comment
    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')