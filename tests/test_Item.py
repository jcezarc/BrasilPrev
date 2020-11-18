import sys
sys.path.append('..')
from service.Item_service import ItemService
from model.Item_model import ItemModel
from util.db.lite_table import LiteTable
from util.tester import Tester

def get_service():
    table = LiteTable(
        ItemModel,{
            'database': Tester.temp_file()
        }
    )
    table.create_table()
    return ItemService(table)

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
