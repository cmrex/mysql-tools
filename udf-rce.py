from sys import flags
from numpy import rint
import pymysql
host = "192.168.191.129"
port = 3306
username = "root"
password = "root"
database = "test"


def udf(host,port,username,password,database):
    try:
        conn = pymysql.connect(user=username, passwd=password,db=database,host=host,port=port)
        print(f"connected with {host}")
    except:
        print("connect error")

if __name__ == '__main__':
    password =  crack(host,port,file,database,username)
    #udf(host,port,username,password,database)
    # mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;z