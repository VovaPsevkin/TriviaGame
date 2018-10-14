import pyodbc
from singletonCreateSQLDB import CreateSQLDB
from createTablesSQLManyToMany import CreateTableInSQLServer
from createProcedure import CreateProcedureToInsertData
from downloadData import DownloadJsonFile
from insertDataTableSQL import InsertDataToTablesSqlServer


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
