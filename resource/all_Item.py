import json
from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from service.Item_service import ItemService

class AllItem(Resource):

    @jwt_required
    def get(self):
        """
        Returns all records from the table Item

        #Read
        """
        service = ItemService()
        return service.find(request.args)
    
    @jwt_required
    def post(self):
        """
        Write a new record in Item

        #Write
        """
        req_data = request.get_json()
        service = ItemService()
        return service.insert(req_data)

    @jwt_required
    def put(self):
        """
        Updates a record in Item

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = ItemService()
        return service.update(req_data)
