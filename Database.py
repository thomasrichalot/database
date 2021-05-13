import mysql.connector
    
class Database():

    def __init__(self, host, user, passwd, database):
        self.mydb = mysql.connector.connect(
        host= host,
        user= user,
        passwd= passwd,
        database= database,)
        self.mycursor = self.mydb.cursor()
    

    def insert_in_db(self, table, column, value):
        formula = ('"INSERT INTO {} ({}) VALUES ({})"'.format(table, column, value))
        print(formula)
        self.mycursor.execute(formula)
        self.mydb.commit()        

database_managment = Database('localhost', 'root', '292810MDs', 'StockList')

create_data_entry = database_managment.insert_in_db('NYSE', 'Ticker', 'AAPL')




