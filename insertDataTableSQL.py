import pyodbc
from singletonCreateSQLdb import CreateSQL_DB
from downloadData import DownloadJsonFile
from createTablesSQLOneToMany import CreateTableInSQLServer


class InsertDataToTableSqlServer:
    """
        Class represent inserting data to SqlServer tables
    """
    def __init__(self):
        pass

    def login_and_transfer_data_toDB(self, json_file):
        # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
        #                     "Server=EXPERISDS1\SQLSERVER2017;" \
        #                     "Database=TriviaQuestions;" \
        #                     "Trusted_Connection=yes;"
        #Home Version
        connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                            "Server=DESKTOP-7DM81V0;" \
                            "Database=TriviaQuestions;" \
                            "Trusted_Connection=yes;"
        connection = pyodbc.connect(connection_string, autocommit=True)
        cursor = connection.cursor()

        for i, j in enumerate(json_file, 1):
            if i < 2:
                print(j)

        cursor.close()
        connection.close()

    @staticmethod
    def drop_tables():
        # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
        #                     "Server=EXPERISDS1\SQLSERVER2017;" \
        #                     "Database=master;" \
        #                     "Trusted_Connection=yes;"
        # Home Version
        connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                            "Server=DESKTOP-7DM81V0;" \
                            "Database=master;" \
                            "Trusted_Connection=yes;"

        sql_query = f"DROP DATABASE TriviaQuestions"
        connection = pyodbc.connect(connection_string, autocommit=True)
        cursor = connection.cursor()
        cursor.execute(sql_query)

        cursor.close()
        connection.close()
    # def login_and_transfer_data_toDB(self, df_question):
    #     """
    #        Insert data into SQLServer table
    #     """
    #
    #     # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
    #     #                     "Server=EXPERISDS1\SQLSERVER2017;" \
    #     #                     "Database=TriviaQuestions;" \
    #     #                     "Trusted_Connection=yes;"
    #     #Home Version
    #     connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
    #                         "Server=DESKTOP-7DM81V0;" \
    #                         "Database=TriviaQuestions;" \
    #                         "Trusted_Connection=yes;"
    #
    #     connection = pyodbc.connect(connection_string, autocommit=True)
    #     cursor = connection.cursor()
    #     sql_query =  f"INSERT INTO { self.table_name} Values (?, ?, ?, ?, ?, ?)"
    #
    #     for index,row in df_question.iterrows():
    #         cursor.execute(sql_query, [row[col] for col in df_question.columns])
    #
    #     #delete dataframe that Created in downloadData module
    #     del df_question
    #
    #     cursor.close()
    #     connection.close()

if __name__ == '__main__':
    # try:
    #     CreateSQL_DB(db_name='TriviaQuestions')
    # except Exception:
    #     print("Database TriviaQuestions already exists")
    #
    # CreateTableInSQLServer().create_table()
    # param = [50, 17, 'medium']
    # jason_file = DownloadJsonFile(*param).internet_data_collect()
    # table = InsertDataToTableSqlServer()
    # table.login_and_transfer_data_toDB(jason_file)

    table = InsertDataToTableSqlServer().drop_tables()
