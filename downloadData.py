import pandas as pd
import json
import requests


class DownloadJsonFile:
    """
        Class represent web operation in python,
        Reading data from the Internet using python library requests,
        Processing using python library json
        Saving data in the data frame by pandas
    """
    def __init__(self, quantity, category, difficulty):
        """
        :param quantity: str, The amount of questions you want to receive
        :param category: str, The subject of the questions
        :param difficulty: str, The difficulty level of the questions
        :param url: str, obj variable, link to an Internet file
        """
        self.url = f"https://opentdb.com/api.php?amount={quantity}" \
                   f"&category={category}&difficulty={difficulty}"

    # def internet_data_collect(self):
    #     """
    #              Reading data from the Internet
    #     :return: dataframe obj, all data from url
    #     """
    #     response = requests.get(self.url)
    #     page = response.text
    #
    #     json_data = json.loads(page)
    #     json_data = json_data["results"]
    #     question = pd.DataFrame(json_data)
    #
    #     #Create TableName to SQLServer Table
    #     self.table_name = json_data[0]["category"].replace('&', '').replace(' ', '') + \
    #                       json_data[0]["difficulty"].title()
    #
    #     #Convert list type in df column to string, SQL table obj cannot containe python list obj
    #     question['incorrect_answers'] = question['incorrect_answers'].apply(lambda x: ' '.join(x))
    #
    #     return question

    def internet_data_collect(self):
        """

        :return: list of dictionaries
        """
        response = requests.get(self.url)
        page = response.text

        json_data = json.loads(page)
        json_data = json_data["results"]
        return json_data


if __name__ == '__main__':
    amount, category, difficulty = 50, 17, 'medium'
    param = [50, 17, 'medium']

    x = DownloadJsonFile(*param)
    question_json_file = x.internet_data_collect()

    for i, j in enumerate(question_json_file, 1):
        if i < 3:
            print(j)

