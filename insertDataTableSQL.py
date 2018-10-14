import pyodbc
from singletonCreateSQLDB import CreateSQLDB
from createTablesSQLManyToMany import CreateTableInSQLServer
from createProcedure import CreateProcedureToInsertData
from downloadData import DownloadJsonFile


#insertDataManyToMany

class InsertDataToTablesSqlServer:
    """
        Class represent inserting data to SqlServer tables
    """
    def __init__(self):
        pass

    def transfer_data_toDB(self, json_file, conn_str):
        sql = "{CALL InsertIntoTables (?, ?, ?, ?, ?, ?) }"
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()
        for json_one in json_file:
            origin = list(json_one.values())
            multiply_incorrect = origin.pop()
            for incorrect in multiply_incorrect:
                origin.append(incorrect)
                cursor.execute(sql, origin)
                cursor.commit()
                origin.remove(incorrect)

        cursor.close()
        connection.close()

    @staticmethod
    def drop_DATABASE():

        connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                            "Server=EXPERISDS1\SQLSERVER2017;" \
                            "Database=master;" \
                            "Trusted_Connection=yes;"
        # Home Version
        # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
        #                    "Server=DESKTOP-7DM81V0;" \
        #                    "Database=master;" \
        #                    "Trusted_Connection=yes;"

        sql_query = f"DROP DATABASE TriviaQuestions"
        connection = pyodbc.connect(connection_string, autocommit=True)
        cursor = connection.cursor()
        cursor.execute(sql_query)

        cursor.close()
        connection.close()


if __name__ == '__main__':

    # try:
    #     CreateSQLDB(db_name='TriviaQuestions')
    # except Exception:
    #     print("Database TriviaQuestions already exists")
    #

    connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                        "Server=EXPERISDS1\SQLSERVER2017;" \
                        "Database=TriviaQuestions;" \
                        "Trusted_Connection=yes;"
    # Home Version
    # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
    #                     "Server=DESKTOP-7DM81V0;" \
    #                     "Database=TriviaQuestions;" \
    #                     "Trusted_Connection=yes;"

    # CreateTableInSQLServer().create_table(conn_str=connection_string)
    # CreateProcedureToInsertData().create_procedure(conn_str=connection_string)
    # param = [50, 17, 'medium']
    # json_file = DownloadJsonFile(*param).internet_data_collect()
    # InsertDataToTablesSqlServer().transfer_data_toDB(json_file=json_file,conn_str=connection_string)

    CreateTableInSQLServer().drop_tables(conn_str=connection_string)
    CreateProcedureToInsertData().drop_procedure(conn_str=connection_string)
    InsertDataToTablesSqlServer().drop_DATABASE()
