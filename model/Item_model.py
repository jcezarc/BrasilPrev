from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Product_model import ProductModel
from model.Purchase_model import PurchaseModel


class ItemModel(Schema):
    id = Integer(primary_key=True, default=0, required=True)
    quantity = Integer(default=1)
    product_id = Nested(ProductModel)
    purchase_id = Nested(PurchaseModel)

