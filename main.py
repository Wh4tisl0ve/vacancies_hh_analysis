import time
from statistics import mean

import numpy as np
import pandas as pd

import src.Analyzer


def main():
    # настройки для полного вывода структур данных
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    # 1 - МСК, 2 - СПБ, 3 - ЕКБ, 4 - Новосибирск, 88 - Казань, 66 - НН,54 - Красноярск, 104 - Челябинск, 78 - Самара, 99 - Уфа
    dict_query = {'most_popular_lang': ['Java', 'C#', 'Python', 'JavaScript', 'C++', 'PHP'],
                  'most_popular_city': [1, 2, 3, 4, 88, 66, 54, 104, 78, 99],
                  'directions_IT': ['Frontend, Backend, Fullstack', 'DevOps', 'Тестировщик',
                                    'Системный администратор']}

    # парсинг данных
    # parser = src.Parser.Parser(dict_query)
    # parser.parsing()
    analyzer = src.Analyzer.Analyzer()
    df = analyzer.get_df_vacancy()

    # подсчет количества вакансий по городам
    # print(df.groupby(by=['keyword','city']).agg('count')['page'])

    # зарплаты
    df_salary = df[['keyword', 'experience','city', 'salary']][df['salary'].notnull()]
    df_salary['salary'] = df_salary['salary'].apply(lambda x: eval(x))
    df_salary['from'] = df_salary['salary'].apply(lambda x: x['from']).fillna(0)
    df_salary['to'] = df_salary['salary'].apply(lambda x: x['to']).fillna(0)
    # в качестве зарплаты берется среднее значение from и to
    df_salary['salaryRes'] = df_salary[['from', 'to']].mean(axis=1)
    print(df_salary[['keyword', 'experience', 'city', 'salaryRes']].groupby(by=['keyword', 'experience', 'city']).agg(['mean', 'min', 'max']))
    # print(df_salary.groupby(by=['keyword']).agg('count'))


if __name__ == "__main__":
    main()
