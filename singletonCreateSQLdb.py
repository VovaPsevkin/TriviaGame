import pyodbc

class CreateSQL_DB:

    class __CreateSQL_DB:
        def __init__(self, db_name):
            self.db_name = db_name
            self.create_data_base()

        def create_data_base(self):
            # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
            #                     "Server=EXPERISDS1\SQLSERVER2017;" \
            #                     "Database=master;" \
            #                     "Trusted_Connection=yes;"

            # Home Version
            connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                                "Server=DESKTOP-7DM81V0;" \
                                "Database=master;" \
                                "Trusted_Connection=yes;"


            connection = pyodbc.connect(connection_string, autocommit=True)
            cursor = connection.cursor()
            query = f"CREATE DATABASE {self.db_name}"
            try:
                cursor.execute(query)
                cursor.close()
                connection.close()
                return True
            except (pyodbc.IntegrityError, pyodbc.ProgrammingError,pyodbc.Error):
                raise Exception(f"Database {self.db_name} already exists. Choose a different database name")


        def __str__(self):
            return repr(self) + self.db_name
    instance = None

    def __init__(self, db_name):

        if not CreateSQL_DB.instance:
            CreateSQL_DB.instance = CreateSQL_DB.__CreateSQL_DB(db_name)
        else:
            CreateSQL_DB.instance.db_name = db_name
    def __getattr__(self, name):
        return getattr(self.instance, name)


if __name__ == '__main__':
    x = CreateSQL_DB(db_name='TriviaQuestions')
    print(x)

