import time
import pandas as pd
import src.Parser


def main():
    # 1 - МСК, 2 - СПБ, 3 - ЕКБ, 4 - Новосибирск, 88 - Казань, 66 - НН,54 - Красноярск, 104 - Челябинск, 78 - Самара, 99 - Уфа
    dict_query = {'most_popular_lang': ['Java', 'C#', 'Python', 'JavaScript', 'C++', 'PHP'],
                  'most_popular_city': [1, 2, 3, 4, 88, 66, 54, 104, 78, 99],
                  'directions_IT': ['Frontend, Backend, Fullstack', 'DevOps', 'Тестировщик',
                                    'Системный администратор']}

    # парсинг данных
    #parser = src.Parser.Parser(dict_query)
    # parser.parsing()

    df_vacanies = pd.read_csv('data.csv', sep=',')
    df_vacanies.columns = ['keyword', 'page', 'id_vacancy', 'name', 'employer', 'accredited_it', 'salary', 'experience',
                           'city', 'created_vacancy', 'skills']
    print(df_vacanies)


if __name__ == "__main__":
    main()
