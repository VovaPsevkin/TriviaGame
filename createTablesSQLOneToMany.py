import pyodbc

from abstractCeateTable import AbsractCreateTable
from singletonCreateSQLdb import CreateSQL_DB


class CreateTableInSQLServer(AbsractCreateTable):
    """
        Class represent create table to SqlServer,
        Create and configure columns in a table (type, Size of each cell)
        and create a primary key
    """

    def __init__(self):
        pass

    def create_table(self):
        """
            insert structure of table on SQL server database
        :return:
        """
        # connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
        #                     "Server=EXPERISDS1\SQLSERVER2017;" \
        #                     "Database=TriviaQuestions;" \
        #                     "Trusted_Connection=yes;"

        connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                            "Server=DESKTOP-7DM81V0;" \
                            "Database=TriviaQuestions;" \
                            "Trusted_Connection=yes;"

        connection = pyodbc.connect(connection_string)
        cursor = connection.cursor()

        sql_query_categories = f"""DROP TABLE IF EXISTS Categories
                                   CREATE TABLE Categories(
                                   CategoryId INT IDENTITY CONSTRAINT pk_categoryId PRIMARY KEY,
                                   CategoryName NVARCHAR(50) CONSTRAINT nt_categoryName NOT NULL
                                  )"""

        cursor.execute(sql_query_categories)
        connection.commit()

        sql_query_type = f"""DROP TABLE IF EXISTS Type
                             CREATE TABLE Type(
                             TypeId INT IDENTITY CONSTRAINT pk_typeId PRIMARY KEY,
                             QuestionType NVARCHAR(120) CONSTRAINT nt_questionType NOT NULL,
                            )"""
        cursor.execute(sql_query_type)
        connection.commit()

        sql_query_difficulty = f"""DROP TABLE IF EXISTS Difficulties
                                   CREATE TABLE Difficulties(
                                   DifficultyID INT IDENTITY CONSTRAINT pk_difficultyId PRIMARY KEY,
                                   Difficulty NVARCHAR(120) CONSTRAINT nt_questionType NOT NULL
                                  )"""
        cursor.execute(sql_query_difficulty)
        connection.commit()

        sql_query_answers = f"""DROP TABLE IF EXISTS Answers
                                CREATE TABLE Answers(
                                AnswersId INT IDENTITY CONSTRAINT pk_answersId PRIMARY KEY,
                                QuestionCorrectAnswer NVARCHAR(50) CONSTRAINT d_questionCorrect DEFAULT NULL,
                                QuestionIncorrectAnswer NVARCHAR(150) CONSTRAINT d_questionIncorrectAnswers DEFAULT NULL   
                               )"""
        cursor.execute(sql_query_answers)
        connection.commit()

        sql_query_questions = f"""DROP TABLE IF EXISTS Questions 
                                  CREATE TABLE Questions(
                                  QuestionId INT IDENTITY CONSTRAINT pk_ProductId PRIMARY KEY,
                                  Question NVARCHAR(150) CONSTRAINT nt_question NOT NULL,
                                  CategoryId INT CONSTRAINT fk_categoryId FOREIGN KEY REFERENCES Categories(CategoryId),
                                  DifficultyID INT CONSTRAINT fk_difficultyId FOREIGN KEY REFERENCES Difficulties(DifficultyID),
                                  TypeId INT CONSTRAINT fk_typeId FOREIGN KEY REFERENCES Type(TypeId),
                                  AnswersId INT CONSTRAINT fk_answersId FOREIGN KEY REFERENCES Answers(AnswersId)
                                 )"""
        cursor.execute(sql_query_questions)
        connection.commit()

        cursor.close()
        connection.close()


if __name__ == '__main__':
    try:
        CreateSQL_DB(db_name='TriviaQuestions')
    except Exception:
        print("Database TriviaQuestions already exists")

    CreateTableInSQLServer().create_table()

