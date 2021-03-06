import sys
sys.path.append('..')
from service.Product_service import ProductService
from model.Product_model import ProductModel
from util.db.lite_table import LiteTable
from util.tester import Tester

def get_service():
    table = LiteTable(
        ProductModel,{
            'database': ':memory:'
        }
    )
    table.create_table()
    return ProductService(table)

def test_find_success():
    test = Tester(get_service)
    test.find_success()

def test_find_failure():
    test = Tester(get_service)
    test.find_failure()

def test_insert_success():
    test = Tester(get_service)
    test.insert_success()

def test_insert_failure():
    test = Tester(get_service)
    test.insert_failure()
