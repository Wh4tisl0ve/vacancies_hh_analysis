import sqlite3

import numpy as np
import pandas as pd
from collections import Counter


# класс, отвечающий за аналитику вакансий
class Analyzer:

    def __init__(self):
        cnt = sqlite3.connect('vacancies.db')
        self.__df_vacancy = pd.read_sql_query("SELECT * FROM vacancies", cnt)
        cnt.close()
        self.__df_vacancy['skills'] = self.__df_vacancy['skills'].apply(lambda x: eval(x))

        # обработка dataframe
        self.__df_vacancy['salary'] = self.__df_vacancy['salary'].fillna('''{'from': 0, 'to': 0, 'currency': 'RUR', 
        'gross': False}''')
        self.__df_vacancy['salary'] = self.__df_vacancy['salary'].apply(lambda x: eval(x))

        # заполнить нулями
        self.__df_vacancy['from'] = self.__df_vacancy['salary'].apply(lambda x: x['from'])
        self.__df_vacancy['to'] = self.__df_vacancy['salary'].apply(lambda x: x['to'])
        self.__df_vacancy['currency'] = self.__df_vacancy['salary'].apply(lambda x: x['currency'])

        # в качестве зарплаты берется среднее значение from и to
        check_na_salary = self.__df_vacancy['from'].notna().any() and self.__df_vacancy['to'].notna().any()
        self.__df_vacancy['salaryRes'] = np.where(check_na_salary,self.__df_vacancy[['from', 'to']].mean(axis=1),0)

        # превратить словарь умений в строку
        self.__df_vacancy['skillsRes'] = self.__df_vacancy['skills'].apply(lambda x: ', '.join([y['name'] for y in x]))

    def get_df_vacancy(self):
        return self.__df_vacancy

    # Подсчет количества вакансий по городам(ключевое слово)
    def get_count_vacancy_by_keyword_city(self) -> pd.DataFrame:
        return self.__df_vacancy.groupby(by=['keyword', 'city']).agg('count')['page']

    # Подсчет количества вакансий по городам
    def get_count_vacancy_by_city(self) -> pd.DataFrame:
        return self.__df_vacancy.groupby(by=['city']).agg('count')['page'].sort_values(ascending=False)

    # Подсчет количества вакансий по компаниям(ТОП-15)
    def get_count_vacancy_by_employer(self) -> pd.DataFrame:
        # круговая диаграмма и проценты
        return self.__df_vacancy.groupby(by='employer').count().sort_values(by='index', ascending=False)[:15]

    # Количество собранных вакансий по годам
    def get_count_vacancy_by_year(self) -> pd.DataFrame:
        return self.__df_vacancy.groupby(by=[pd.DatetimeIndex(self.__df_vacancy['created_vacancy'])
                                         .year]).agg('count')['keyword']

    # Подсчет информации по зарплатам(в рублях)
    def get_agg_salary(self) -> pd.DataFrame:
        df_salary = self.__df_vacancy[['keyword', 'experience', 'city', 'salary']][
            self.__df_vacancy['salary'].notnull()]

        return (df_salary[df_salary['currency'] == 'RUR'][['keyword', 'experience', 'city', 'salaryRes']]
                .groupby(by=['keyword', 'experience', 'city']).agg(['mean', 'min', 'max', 'count']))

    def get_dict_keyword(self) -> dict:
        dict_keyword = {}

        for item in self.__df_vacancy.itertuples():
            dict_keyword[item[1]] = []

        return dict_keyword

    # Самые популярные технологии которые встречаются в вакансиях
    def get_popular_skills(self) -> dict:
        dict_popular_skills = self.get_dict_keyword()

        for key in dict_popular_skills.keys():
            list_skills_lang = []
            for i, in self.__df_vacancy[['skills']][self.__df_vacancy['keyword'] == key].values:
                for j in i:
                    list_skills_lang.append({j['name']: 1})
            dict_popular_skills[key] = list_skills_lang

            all_keys = [key for d in dict_popular_skills[key] for key in d.keys()]

            # Считаем частоту каждого ключа
            word_freq = dict(Counter(all_keys))

            dict_popular_skills[key] = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

        return dict_popular_skills
