import pyodbc
from collections import OrderedDict
from downloadData import DownloadJsonFile



def insert_categories(name):
    # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
    #                     "Server=EXPERISDS1\SQLSERVER2017;" \
    #                     "Database=TriviaQuestions;" \
    #                     "Trusted_Connection=yes;"
    # Home Version
    connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                        "Server=DESKTOP-7DM81V0;" \
                        "Database=TriviaQuestions;" \
                        "Trusted_Connection=yes;"
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    sql_query = f"""
                  INSERT INTO Categories(CategoryName)
                  Select ? WHERE NOT EXISTS(SELECT * FROM Categories WHERE CategoryName=?)
                """
    inserted = cursor.execute(sql_query, name, name).rowcount
    connection.commit()
    cursor.close()
    connection.close()
    return inserted


param = [50, 17, 'medium']
jason_file = DownloadJsonFile(*param).internet_data_collect()

for i, json_one in enumerate(jason_file, 1):
    one = OrderedDict(sorted(json_one.items(), key=lambda x: x[0]))
    if i < 2:
        keys, val = list(zip(*one.items()))
        # print(f,end='\n\n')
        for j, key in enumerate(keys,1):
            if j < 2:
                print(key)
                name = one[key]
                print(name, end='\n\n')
                insert_categories(name)
