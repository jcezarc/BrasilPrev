import sys
sys.path.append('..')
from service.Customer_service import CustomerService
from model.Customer_model import CustomerModel
from util.db.lite_table import LiteTable
from util.tester import Tester

def get_service():
    table = LiteTable(
        CustomerModel,{
            'database': ':memory:'
        }
    )
    table.create_table()
    return CustomerService(table)

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
