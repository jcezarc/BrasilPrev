import json
from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from service.Product_service import ProductService

class AllProduct(Resource):

    # @jwt_required
    def get(self):
        """
        Returns all records from the table Product

        #Read
        """
        service = ProductService()
        return service.find(request.args)
    
    # @jwt_required
    def post(self):
        """
        Write a new record in Product

        #Write
        """
        req_data = request.get_json()
        service = ProductService()
        return service.insert(req_data)

    # @jwt_required
    def put(self):
        """
        Updates a record in Product

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = ProductService()
        return service.update(req_data)
