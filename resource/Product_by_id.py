from flask_restful import Resource
from flask_jwt_extended import jwt_required
from service.Product_service import ProductService

class ProductById(Resource):

    @jwt_required
    def get(self, id):
        """
        Search in  Product by the field id

        #Read
        """
        service = ProductService()
        return service.find(None, id)

    @jwt_required
    def delete(self, id):
        """
        Delete a record of Product

        #Write
        """
        service = ProductService()
        return service.delete([id])
