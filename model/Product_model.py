from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean


class ProductModel(Schema):
    id = Integer(primary_key=True, default=0, required=True)
    name = Str()
    value = Float()


