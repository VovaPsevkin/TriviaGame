import pyodbc

from abstractCeateTable import AbsractCreateTable
from singletonCreateSQLDB import CreateSQLDB


class CreateTableInSQLServer(AbsractCreateTable):
    """
            Class represent create table to SqlServer,
            Create and configure columns in a table (type, Size of each cell)
            and create a primary key
    """
    def __init__(self):
        pass

    def create_table(self, conn_str):
        """
             insert structure of tables on SQL server database
             (Diagram Many-to-Many
        :param conn_str: string to connect to SQLServer
        :return: None
        """
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()

        sql_query = f"""DROP TABLE IF EXISTS Questions 
                        CREATE TABLE Questions
                        (
	                        QuestionId INT IDENTITY CONSTRAINT pk_uestionId PRIMARY KEY,
	                        Question NVARCHAR(150) CONSTRAINT nt_question NOT NULL
                        )
                        DROP TABLE IF EXISTS Difficulties
                        CREATE TABLE Difficulties
                        (
	                        DifficultyID INT IDENTITY CONSTRAINT pk_difficultyId PRIMARY KEY,
                            Difficulty NVARCHAR(20) CONSTRAINT nt_difficultType NOT NULL
                        )
                        DROP TABLE IF EXISTS DifficultiesQuestions
                        CREATE TABLE DifficultiesQuestions
                        (
	                        QuestionID INT NOT NULL CONSTRAINT fk_questionID 
	                            FOREIGN KEY REFERENCES Questions(QuestionId),
	                        DifficultyID INT NOT NULL  CONSTRAINT fk_difficultyID 
	                            FOREIGN KEY REFERENCES Difficulties(DifficultyID),
	                        PRIMARY KEY CLUSTERED (QuestionID,DifficultyID)
                        )		
                        DROP TABLE IF EXISTS Categories
                        CREATE TABLE Categories
                        (
	                        CategoryId INT IDENTITY CONSTRAINT pk_categoryId PRIMARY KEY,
                            Category NVARCHAR(50) CONSTRAINT nt_category NOT NULL
                        )	
                        DROP TABLE IF EXISTS CategoriesQuestions
                        CREATE TABLE CategoriesQuestions
                        (
	                        QuestionID INT NOT NULL CONSTRAINT fk_catquestionID 
	                            FOREIGN KEY REFERENCES Questions(QuestionId),
	                        CategoryId INT NOT NULL  CONSTRAINT fk_categoryId 
	                            FOREIGN KEY REFERENCES Categories(CategoryId),
	                        PRIMARY KEY CLUSTERED (QuestionID,CategoryId)
                        )
                        DROP TABLE IF EXISTS QTypes
                        CREATE TABLE QTypes
                        (
	                        TypeId INT IDENTITY CONSTRAINT pk_typeId PRIMARY KEY,
                            QuestionType NVARCHAR(120) CONSTRAINT nt_questionType NOT NULL
                        )	
                        DROP TABLE IF EXISTS TypesQuestions
                        CREATE TABLE TypesQuestions
                        (
	                        QuestionID INT NOT NULL CONSTRAINT fk_typequestionID 
	                            FOREIGN KEY REFERENCES Questions(QuestionId),
	                        TypeId INT NOT NULL  CONSTRAINT fk_typeId 
	                            FOREIGN KEY REFERENCES QTypes(TypeId),
	                        PRIMARY KEY CLUSTERED (QuestionID,TypeId)
                        )
                        DROP TABLE IF EXISTS Answers
                        CREATE TABLE Answers
                        (
	                        AnswersId INT IDENTITY CONSTRAINT pk_answersId PRIMARY KEY,
	                        QuestionCorrectAnswer NVARCHAR(150) 
	                            CONSTRAINT d_questionCorrect DEFAULT NULL,
	                        QuestionIncorrectAnswer NVARCHAR(150) 
	                            CONSTRAINT nt_questionIncorrectAnswers NOT NULL   
                        )
                        DROP TABLE IF EXISTS AnswersQuestions
                        CREATE TABLE AnswersQuestions
                        (
	                        QuestionID INT NOT NULL CONSTRAINT fk_ansquestionID 
	                            FOREIGN KEY REFERENCES Questions(QuestionId),
	                        AnswersId INT NOT NULL  CONSTRAINT fk_answersId 
	                            FOREIGN KEY REFERENCES Answers(AnswersId),
	                        PRIMARY KEY CLUSTERED (QuestionID,AnswersId)
                        )"""
        cursor.execute(sql_query)
        connection.commit()
    def drop_tables(self,conn_str):
        """

        :param conn_str: string to connect to SQLServer
        :return: None
        """
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()

        sql_query = f"""DROP TABLE AnswersQuestions
                        DROP TABLE CategoriesQuestions
                        DROP TABLE DifficultiesQuestions
                        DROP TABLE TypesQuestions
                        DROP TABLE Answers
                        DROP TABLE Categories
                        DROP TABLE QTypes
                        DROP TABLE Difficulties
                        DROP TABLE Questions
                    """
        cursor.execute(sql_query)
        connection.commit()

if __name__ == '__main__':
    connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                        "Server=EXPERISDS1\SQLSERVER2017;" \
                        "Database=TriviaQuestions;" \
                        "Trusted_Connection=yes;"

    # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
    #                     "Server=DESKTOP-7DM81V0;" \
    #                     "Database=TriviaQuestions;" \
    #                     "Trusted_Connection=yes;"

    try:
        CreateSQLDB(db_name='TriviaQuestions')
    except Exception:
        print("Database TriviaQuestions already exists")
    #CreateTableInSQLServer().create_table(conn_str=connection_string)
    CreateTableInSQLServer().drop_tables(conn_str=connection_string)
