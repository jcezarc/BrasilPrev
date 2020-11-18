import json
from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from service.Customer_service import CustomerService

class AllCustomer(Resource):

    @jwt_required
    def get(self):
        """
        Returns all records from the table Customer

        #Read
        """
        service = CustomerService()
        return service.find(request.args)
    
    @jwt_required
    def post(self):
        """
        Write a new record in Customer

        #Write
        """
        req_data = request.get_json()
        service = CustomerService()
        return service.insert(req_data)

    @jwt_required
    def put(self):
        """
        Updates a record in Customer

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = CustomerService()
        return service.update(req_data)
