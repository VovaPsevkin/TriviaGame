from singletonCreateSQLdb import CreateSQL_DB
from createTablesSQLOneToMany import CreateTableInSQLServer
from insertDataTableSQL import InsertDataToTableSqlServer
from downloadData import DownloadJsonFile

amount, category, difficulty = 50, 17, 'medium'

x = DownloadJsonFile(amount, category, difficulty)
question_df = x.internet_data_collect()
table_name = x.table_name

try :
    CreateSQL_DB(db_name='TriviaQuestions')
except Exception:
    print("Database TriviaQuestions already exists")

#print(question_df.head())

x = CreateTableInSQLServer(table_name)
x.create_table()

y = InsertDataToTableSqlServer(table_name)
y.login_and_transfer_data_toDB(question_df)
#
