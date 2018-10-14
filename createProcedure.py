import pyodbc
class CreateProcedureToInsertData():

    def create_procedure(self, conn_str):

        connection = pyodbc.connect(conn_str,autocommit=True)
        cursor = connection.cursor()

        sql_query = f"""CREATE PROCEDURE InsertIntoTables
                        @Category NVARCHAR(50),
                        @Type NVARCHAR(50),
                        @Difficulty NVARCHAR(50),
                        @Question NVARCHAR(150), 
                        @Correct NVARCHAR(50),
                        @InCorrect NVARCHAR(50)
                        AS
                        BEGIN
	                        DECLARE @QuestionID INT
	                        DECLARE @DifficultyID INT
	                        DECLARE @CategoryID INT
	                        DECLARE @TypeID INT
	                        DECLARE @AnswerID INT


	                        SELECT @QuestionID = QuestionID FROM Questions WHERE Question = @Question
	                        IF(@QuestionID IS NULL )
	                        BEGIN
		                        INSERT INTO Questions VALUES(@Question)
		                        SELECT @QuestionID = SCOPE_IDENTITY()
	                        END

	                        SELECT @DifficultyID = DifficultyID FROM DIFficulties WHERE Difficulty = @Difficulty
	                        IF(@DifficultyID IS NULL )
	                        BEGIN
		                        INSERT INTO DIFficulties VALUES(@Difficulty)
		                        SELECT @DifficultyID = SCOPE_IDENTITY()
	                        END

                    	    SELECT @CategoryID = CategoryID FROM Categories WHERE Category = @Category
	                        IF(@CategoryID IS NULL )
	                        BEGIN
		                        INSERT INTO Categories VALUES(@Category)
		                        SELECT @CategoryID = SCOPE_IDENTITY()
	                        END

	                        SELECT @TypeID = TypeId FROM QTypes WHERE QuestionType = @Type
	                        IF(@TypeID IS NULL )
	                        BEGIN
		                        INSERT INTO QTypes VALUES(@Type)
		                        SELECT @TypeID = SCOPE_IDENTITY()
	                        END

	                        SELECT @AnswerID = AnswersId FROM Answers
	                        WHERE (QuestionCorrectAnswer = @Correct AND QuestionIncorrectAnswer = @InCorrect)
		                    OR (QuestionCorrectAnswer IS NULL AND QuestionIncorrectAnswer = @InCorrect)
	                        IF(@AnswerID IS NULL )
	                        BEGIN
		                        INSERT INTO Answers VALUES(@Correct, @InCorrect)
		                        SELECT @AnswerID = SCOPE_IDENTITY()
        	                END

 
	                        INSERT INTO AnswersQuestions VALUES(@QuestionID, @AnswerID)
	                        INSERT INTO CategoriesQuestions VALUES(@QuestionID, @CategoryID)
	                        INSERT INTO DifficultiesQuestions VALUES(@QuestionID, @DifficultyID)
	                        INSERT INTO TypesQuestions VALUES(@QuestionID, @TypeID)

                        END"""
        cursor.execute(sql_query)
        cursor.close()
        connection.close()


    def drop_procedure(self,conn_str):
        connection = pyodbc.connect(conn_str, autocommit=True)
        cursor = connection.cursor()
        sql_query = f"""DROP PROCEDURE IF EXISTS spInsertINToQuestionsDifficulties"""

        cursor.execute(sql_query)
        cursor.close()
        connection.close()

if __name__ == '__main__':
    connection_string = "Driver={ODBC Driver 13 for SQL Server};" \
                        "Server=EXPERISDS1\SQLSERVER2017;" \
                        "Database=TriviaQuestions;" \
                        "Trusted_Connection=yes;"

    x = CreateProcedureToInsertData()
    #x.create_procedure(conn_str=connection_string)
    #x.drop_procedure(conn_str=connection_string)