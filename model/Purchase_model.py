from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Customer_model import CustomerModel


class PurchaseModel(Schema):
    id = Integer(primary_key=True, default=0, required=True)
    sale_date = Date()
    customer_id = Nested(CustomerModel)

