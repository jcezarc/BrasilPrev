from flask_restful import Resource
from flask_jwt_extended import jwt_required
from service.Customer_service import CustomerService

class CustomerById(Resource):

    # @jwt_required
    def get(self, id):
        """
        Search in  Customer by the field id

        #Read
        """
        service = CustomerService()
        return service.find(None, id)

    # @jwt_required
    def delete(self, id):
        """
        Delete a record of Customer

        #Write
        """
        service = CustomerService()
        return service.delete([id])
