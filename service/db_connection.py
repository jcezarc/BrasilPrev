import os
from util.db.lite_table import LiteTable

# ----------------------------------------------
SALES_USER = os.environ.get(
    'SALES_USER',
    '<<** Coloque aqui seu usuário **>>'
)
SALES_PASSWORD = os.environ.get(
    'SALES_PASSWORD',
    '<<** Coloque aqui sua senha **>>'
)
SALES_HOST = os.environ.get(
    'SALES_HOST',
    'localhost'
)
# ----------------------------------------------

def get_table(schema):
    return LiteTable(schema, {
        # ---- MySql -------------------------
            # "host": SALES_HOST,
            # "user": SALES_USER,
            # "password": SALES_PASSWORD,
            # "database": "sales"
        # ---- Sqlite -----------------------
                    "database": "sales.db"
        })
