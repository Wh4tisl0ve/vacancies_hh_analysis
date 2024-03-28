import time
from statistics import mean
from collections import Counter
import numpy as np
import pandas as pd

import src.Analyzer


def main():
    # настройки для полного вывода структур данных
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)

    # dict_query = {'most_popular_lang': ['Java', 'C#', 'Python', 'JavaScript', 'C++', 'PHP'],
    #               'most_popular_city': [1, 2, 3, 4, 88, 66, 54, 104, 78, 99],
    #               'directions_IT': ['Frontend, Backend, Fullstack', 'DevOps', 'Тестировщик',
    #                                 'Системный администратор']}
    # парсинг данных
    # parser = src.Parser.Parser(dict_query)
    # parser.parsing()
    analyzer = src.Analyzer.Analyzer()
    df = analyzer.get_df_vacancy()

    # 1. подсчет количества вакансий по городам
    # print(df.groupby(by=['keyword','city']).agg('count')['page'])

    # 2. количество собранных вакансий по годам
    # print(df.groupby(by=[pd.DatetimeIndex(df['created_vacancy']).year]).agg('count')['keyword'])

    # 3. подсчет информации по зарплатам
    # df_salary = df[['keyword', 'experience', 'city', 'salary']][df['salary'].notnull()]
    # # обработка dataframe
    # df_salary['salary'] = df_salary['salary'].apply(lambda x: eval(x))
    # df_salary['from'] = df_salary['salary'].apply(lambda x: x['from']).fillna(0)
    # df_salary['to'] = df_salary['salary'].apply(lambda x: x['to']).fillna(0)
    # # в качестве зарплаты берется среднее значение from и to
    # df_salary['salaryRes'] = df_salary[['from', 'to']].mean(axis=1)
    # print(df_salary[['keyword', 'experience', 'city', 'salaryRes']].groupby(by=['keyword', 'experience', 'city']).agg(['mean', 'min', 'max']))
    # print(df_salary.groupby(by=['keyword']).agg('count'))

    # 4. Самые популярные технологии которые встречаются в вакансиях

    df_skills = df[['keyword', 'experience', 'city', 'skills']]
    dict_popular_skills = {}

    for item in df_skills.itertuples():
        dict_popular_skills[item[1]] = []

    for key in dict_popular_skills.keys():
        list_skills_lang = []
        for i, in df_skills[['skills']][df['keyword'] == key].values:
            for j in i:
                list_skills_lang.append({j['name']: 1})
        dict_popular_skills[key] = list_skills_lang

        # Извлекаем все ключи из словарей и объединяем их
        all_keys = [key for d in dict_popular_skills[key] for key in d.keys()]

        # Считаем частоту каждого ключа
        word_freq = dict(Counter(all_keys))

        print(sorted(word_freq.items(), key=lambda x:x[1], reverse=True)[:10])



if __name__ == "__main__":
    main()
