import pandas as pd
from collections import Counter


# класс, отвечающий за аналитику вакансий
class Analyzer:

    def __init__(self):
        self.__df_vacancy = pd.read_csv('data.csv', sep=',')
        self.__df_vacancy.columns = ['keyword', 'page', 'id_vacancy', 'name',
                                     'employer', 'accredited_it', 'salary',
                                     'experience', 'city', 'created_vacancy', 'skills']
        self.__df_vacancy['skills'] = self.__df_vacancy['skills'].apply(lambda x: eval(x))
        # настройки для полного вывода структур данных
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_colwidth', None)

    def get_df_vacancy(self):
        return self.__df_vacancy

    # Подсчет количества вакансий по городам
    def get_count_vacancy_by_city(self) -> pd.DataFrame:
        return self.__df_vacancy.groupby(by=['keyword', 'city']).agg('count')['page']

    # Количество собранных вакансий по годам
    def get_count_vacancy_by_year(self) -> pd.DataFrame:
        return self.__df_vacancy.groupby(by=[pd.DatetimeIndex(self.__df_vacancy['created_vacancy'])
                                         .year]).agg('count')['keyword']

    # Подсчет информации по зарплатам(в рублях)
    def get_agg_salary(self) -> pd.DataFrame:
        df_salary = self.__df_vacancy[['keyword', 'experience', 'city', 'salary']][
            self.__df_vacancy['salary'].notnull()]

        # обработка dataframe
        df_salary['salary'] = df_salary['salary'].apply(lambda x: eval(x))
        df_salary['from'] = df_salary['salary'].apply(lambda x: x['from']).fillna(0)
        df_salary['to'] = df_salary['salary'].apply(lambda x: x['to']).fillna(0)
        df_salary['currency'] = df_salary['salary'].apply(lambda x: x['currency'])

        # в качестве зарплаты берется среднее значение from и to
        df_salary['salaryRes'] = df_salary[['from', 'to']].mean(axis=1)

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

    # Подсчет количества вакансий по компаниям(ТОП-15)
    def get_count_vacancy_by_employer(self) -> pd.DataFrame:
        # круговая диаграмма и проценты
        return self.__df_vacancy.groupby(by='employer').agg('count')['page'].sort_values(ascending=False)[:15]
