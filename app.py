# -*- coding: utf-8 -*-
import os
import logging
import uuid
from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import create_access_token, JWTManager
import sys
sys.path.append('.')
from resource.user_controller import valid_user
from util.swagger_generator import FlaskSwaggerGenerator
from model.Customer_model import CustomerModel
from resource.Customer_by_id import CustomerById
from resource.all_Customer import AllCustomer
from model.Product_model import ProductModel
from resource.Product_by_id import ProductById
from resource.all_Product import AllProduct
from model.Purchase_model import PurchaseModel
from resource.Purchase_by_id import PurchaseById
from resource.all_Purchase import AllPurchase
from model.Item_model import ItemModel
from resource.Item_by_id import ItemById
from resource.all_Item import AllItem


BASE_PATH = '/Sales'


def config_routes(app):
    api = Api(app)
    # --- Resources: ----
    api.add_resource(CustomerById, f'{BASE_PATH}/Customer/<id>',
                     methods=['GET'], endpoint='get_Customer_by_id')
    api.add_resource(AllCustomer, f'{BASE_PATH}/Customer',
                     methods=['GET'], endpoint='get_AllCustomer')
    api.add_resource(AllCustomer, f'{BASE_PATH}/Customer',
                     methods=['POST'], endpoint='post_Customer')
    api.add_resource(
        AllCustomer,
        f'{BASE_PATH}/Customer',
        methods=['PUT'],
        endpoint='put_Customer'
    )
    api.add_resource(CustomerById, f'{BASE_PATH}/Customer/<id>',
                     methods=['DELETE'], endpoint='delete_Customer')
    api.add_resource(ProductById, f'{BASE_PATH}/Product/<id>',
                     methods=['GET'], endpoint='get_Product_by_id')
    api.add_resource(AllProduct, f'{BASE_PATH}/Product',
                     methods=['GET'], endpoint='get_AllProduct')
    api.add_resource(AllProduct, f'{BASE_PATH}/Product',
                     methods=['POST'], endpoint='post_Product')
    api.add_resource(AllProduct, f'{BASE_PATH}/Product',
                     methods=['PUT'], endpoint='put_Product')
    api.add_resource(ProductById, f'{BASE_PATH}/Product/<id>',
                     methods=['DELETE'], endpoint='delete_Product')
    api.add_resource(PurchaseById, f'{BASE_PATH}/Purchase/<id>',
                     methods=['GET'], endpoint='get_Purchase_by_id')
    api.add_resource(AllPurchase, f'{BASE_PATH}/Purchase',
                     methods=['GET'], endpoint='get_AllPurchase')
    api.add_resource(AllPurchase, f'{BASE_PATH}/Purchase',
                     methods=['POST'], endpoint='post_Purchase')
    api.add_resource(AllPurchase, f'{BASE_PATH}/Purchase',
                     methods=['PUT'], endpoint='put_Purchase')
    api.add_resource(PurchaseById, f'{BASE_PATH}/Purchase/<id>',
                     methods=['DELETE'], endpoint='delete_Purchase')
    api.add_resource(ItemById, f'{BASE_PATH}/Item/<id>',
                     methods=['GET'], endpoint='get_Item_by_id')
    api.add_resource(AllItem, f'{BASE_PATH}/Item',
                     methods=['GET'], endpoint='get_AllItem')
    api.add_resource(AllItem, f'{BASE_PATH}/Item',
                     methods=['POST'], endpoint='post_Item')
    api.add_resource(AllItem, f'{BASE_PATH}/Item',
                     methods=['PUT'], endpoint='put_Item')
    api.add_resource(ItemById, f'{BASE_PATH}/Item/<id>',
                     methods=['DELETE'], endpoint='delete_Item')

    # -------------------


def set_swagger(app):
    swagger_url = '/docs'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        '/api',
        config={
            'app_name': "*- Sales -*"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)


def swagger_details(args):
    id_route = args[0]
    params = args[1]
    model = None
    resource = None
    docstring = ""
    if id_route == 'docs':
        docstring = """Swagger documentation
        #Doc
        """
    elif id_route == 'Customer':
        if not params:
            resource = AllCustomer
        else:
            resource = CustomerById
        model = CustomerModel()
    elif id_route == 'Product':
        if not params:
            resource = AllProduct
        else:
            resource = ProductById
        model = ProductModel()
    elif id_route == 'Purchase':
        if not params:
            resource = AllPurchase
        else:
            resource = PurchaseById
        model = PurchaseModel()
    elif id_route == 'Item':
        if not params:
            resource = AllItem
        else:
            resource = ItemById
        model = ItemModel()
    ignore = False
    return model, resource, docstring, ignore


logging.basicConfig(
    filename='Sales.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

APP = Flask(__name__)
CORS(APP)
APP.config['JWT_SECRET_KEY'] = str(uuid.uuid4())
JWT = JWTManager(APP)
config_routes(APP)
set_swagger(APP)


@APP.route('/api')
def get_api():
    """
    API json data

    #Doc
    """
    generator = FlaskSwaggerGenerator(
        swagger_details,
        None
    )
    return jsonify(generator.content)


@APP.route('/health')
def health():
    return 'OK', 200


@APP.route('/handshake', methods=['POST'])
def hand_shake():
    """
    Grant access to API endpoints

    #Access
    """
    user = request.json.get('user')
    password = request.json.get('password')
    found, user_id = valid_user(user, password)
    if not found:
        return "Invalid user", 403
    access_token = create_access_token(identity=user_id)
    return jsonify(access_token=access_token), 200


if __name__ == '__main__':
    APP.run(
        debug=True,
        port=os.environ.get('SALES_PORT', 5000),
        host='0.0.0.0'
    )
