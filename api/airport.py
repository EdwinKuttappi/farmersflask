from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building

from model.airportmodel import AirportPost

airport_api = Blueprint('airport_api', __name__,
                   url_prefix='/api/airport')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(airport_api)

class AirportPostAPI(Resource):        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            # validate name
            city = body.get('city')
            airport = body.get('airport')
   
            ''' #1: Key code block, setup USER OBJECT '''
            uo = AirportPost(city=city, airport=airport)
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {city}, format error'}, 210

    class _Read(Resource):
        def get(self):
            users = AirportPost.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Delete(Resource):
        def delete(self):
            ''' Read data for json body '''
            body = request.get_json()
            city = body.get('city')

            airports = AirportPost.query.all()    # read/extract all users from database
            
            # Find the city in the database and call the delete
            for airport in airports:
                if airport.city == city:
                    airport.delete()
                    return
            
            # delete operation does not return any value
            return {'message': f' {city} is not in database'}, 210

        
    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')
