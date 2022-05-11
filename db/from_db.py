import pandas as pd
import warnings
from sqlalchemy import create_engine
warnings.filterwarnings('ignore')

# db connect
user = "chipnday"
password = "chipnday2022"
host = "132.226.150.234:3306"
db = "chipnday_db"
db_connection_str = f'mysql+pymysql://{user}:{password}@{host}/{db}'
encoding = '?charset="utf8", encoding="utf-8"'
db_connection = create_engine(db_connection_str)
conn = db_connection.connect()


# df -> db insert
def db_select(table):
    df = pd.read_sql_table(table, db_connection)
    return df
