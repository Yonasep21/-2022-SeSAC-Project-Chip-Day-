import warnings

warnings.filterwarnings('ignore')
import pymysql

# db connect
user = "chipnday"
password = "chipnday2022"
host = "132.226.150.234"
port = 3306
db = "chipnday_db"
encoding = 'utf8'
# return dict
db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=encoding, autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)
#origianl
#db = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=encoding)

def conn():
    return db

def cursor():
    return db.cursor()
