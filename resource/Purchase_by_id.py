from flask_restful import Resource
from flask_jwt_extended import jwt_required
from service.Purchase_service import PurchaseService

class PurchaseById(Resource):

    # @jwt_required
    def get(self, id):
        """
        Search in  Purchase by the field id

        #Read
        """
        service = PurchaseService()
        return service.find(None, id)

    # @jwt_required
    def delete(self, id):
        """
        Delete a record of Purchase

        #Write
        """
        service = PurchaseService()
        return service.delete([id])
