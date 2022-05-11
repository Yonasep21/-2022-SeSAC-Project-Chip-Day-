import pandas as pd
import warnings
from sqlalchemy import create_engine
import re
import requests
import random
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
def db_insert(df, table):
    # 중복제거
    old_df = pd.read_sql_table(table, db_connection)
    sum_df = pd.concat([old_df, df], ignore_index=True)
    if table == 'MovieInfo':
        sum_df = sum_df.drop_duplicates(subset=['KinoId'])
    if table == 'MovieReview':
        sum_df = sum_df.drop_duplicates(subset=['ReviewTitle'])
    if table == 'ImgUrl':
        if 'OgImg' in df :
            sum_df = sum_df.dropna(axis=0)
            sum_df = sum_df.drop_duplicates(subset=['OgImg'])
        else:
            sum_df = sum_df.drop_duplicates(subset=['SmallImg'])
    row = sum_df.to_sql(name=table, con=db_connection, if_exists='replace', index=False)
    print(f'{table} :: {row} insert success')
