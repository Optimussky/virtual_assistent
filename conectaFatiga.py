import mysql.connector as mysql
from mysql.connector import errorcode


class Database(object):
    def __init__(self, host, user, user_pass, database_name):
        self.host, self.database_name = host, database_name
        self.user, self.user_pass = user, user_pass
        try:
            self.connect = mysql.connect(
                host= host, user= user,
                passwd= user_pass, database= database_name
            )
            print("Successfully connected to database: {}.".format(database_name))
            self.cursor = self.connect.cursor()
            #self.tables = self.get_all_tables()

        except mysql.Error as err:
            print(err)


        def get_sector(self):  #<-- expects a string and a list of tuples
            command = 'SELECT nombre,usuario,clave from tbUsuario;'
            
            try:
                result = self.cursor.execute(command)
                print(f'{result}')
                print(result)
            except mysql.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("Bad Error here!")
                else:
                    print(err)



"""
    def create_table(self, table_name, columns):  #<-- expects a string and a list of tuples
        command = ['{} {}'.format(col[0], col[1]) for col in columns]
        command = ', '.join(command)
        try:
            self.cursor.execute("CREATE TABLE {} ({});".format(table_name, command))
            print("Table \"{}\" successfully created.".format(table_name))
        except mysql.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table \"{}\" already exists.".format(table_name))
            else:
                print(err)


    def remove_table(self, table_name):
        try:
            self.cursor.execute("DROP TABLE {};".format(table_name))
            print("Table \"{}\" removed.".format(table_name))
        except mysql.Error as err:
            print(err)
            """


if __name__ == "__main__":
    #Configuring the database
    DATABASE_NAME = 'dbfatiga'
    config = {
        'host': 'localhost',
        'user': 'fatiga',
        'pass': 'F4t1g4',
        'db': DATABASE_NAME  # <-- Connects to database accounts
        }
    db = Database(config['host'], config['user'],
                  config['pass'], config['db'])

    