### importing Mysql connector for connecting with Server
import mysql.connector

### Acessing the Database
mydb_gk = mysql.connector.connect(host ='localhost',user ='root',passwd='1234',database = 'testdb')
mycursor_gk = mydb_gk.cursor()

### Query function which queries output from database
def query_(query):

    sql = "SELECT Files FROM Data_base WHERE Tag = '"+query+"' "
    mycursor_gk.execute(sql)
    myre = mycursor_gk.fetchall()
    for r in myre:
        print(r)

