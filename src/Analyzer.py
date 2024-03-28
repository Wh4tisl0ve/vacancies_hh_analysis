import pandas as pd


class Analyzer:

    def __init__(self):
        self.__df_vacancy = pd.read_csv('data.csv', sep=',')
        self.__df_vacancy.columns = ['keyword', 'page', 'id_vacancy', 'name',
                                     'employer', 'accredited_it', 'salary',
                                     'experience', 'city', 'created_vacancy', 'skills']
        self.__df_vacancy['skills'] = self.__df_vacancy['skills'].apply(lambda x: eval(x))

    def get_df_vacancy(self):
        return self.__df_vacancy
