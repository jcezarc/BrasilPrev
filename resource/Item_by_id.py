from flask_restful import Resource
from flask_jwt_extended import jwt_required
from service.Item_service import ItemService

class ItemById(Resource):

    @jwt_required
    def get(self, id):
        """
        Search in  Item by the field id

        #Read
        """
        service = ItemService()
        return service.find(None, id)

    @jwt_required
    def delete(self, id):
        """
        Delete a record of Item

        #Write
        """
        service = ItemService()
        return service.delete([id])
