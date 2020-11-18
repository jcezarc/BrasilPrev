import json
from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from service.Purchase_service import PurchaseService

class AllPurchase(Resource):

    # @jwt_required
    def get(self):
        """
        Returns all records from the table Purchase

        #Read
        """
        service = PurchaseService()
        return service.find(request.args)
    
    # @jwt_required
    def post(self):
        """
        Write a new record in Purchase

        #Write
        """
        req_data = request.get_json()
        service = PurchaseService()
        return service.insert(req_data)

    # @jwt_required
    def put(self):
        """
        Updates a record in Purchase

        #Write
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = PurchaseService()
        return service.update(req_data)
