import mysql.connector as connector
from times import Time

class Db:
    def __init__(self):
        self.connection = connector.connect(host='localhost',
                  port=3306,user='root',
                  password='Swastik07@#',
                  database='swastik')
        self.cur = self.connection.cursor()
        #self.cur.execute('create table Screentimehistory (started varchar(10),ended varchar(10),timestamp varchar(10))')
        
    def insert(self,data):
        print(data)
        if self.cur:
            self.cur.execute("insert into swastik.screentimehistory (started,ended,timestamp) values (%s,%s,%s)",(data[0],data[1],data[2]))
            self.connection.commit()
    
    def gethistory(self):
        cur = self.connection.cursor()
        cur.execute('select * from swastik.screentimehistory')
        return cur.fetchall()

            
            
        
        
        

