import sys
sys.path.append('..')
from service.Purchase_service import PurchaseService
from model.Purchase_model import PurchaseModel
from util.db.lite_table import LiteTable
from util.tester import Tester

def get_service():
    table = LiteTable(
        PurchaseModel,{
            'database': Tester.temp_file()
        }
    )
    table.create_table()
    table.allow_left_joins = False
    return PurchaseService(table)

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
