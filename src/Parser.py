import time

import src.ApiHH
import src.FileHandler


class Parser:
    def __init__(self, dict_query):
        # адрес запроса
        self.__dict_query = dict_query

    def parsing(self):
        parser = src.ApiHH.ApiHH()
        csv_handler = src.FileHandler.CSVHandler()

        for lang in self.__dict_query['most_popular_lang']:
            for city in self.__dict_query['most_popular_city']:
                for page in range(0, 10):
                    params = parser.get_vacancies_params(text=lang, city=city, page=page)
                    headers = parser.get_headers()
                    data = parser.get_vacancy_request(params, headers)
                    for item in data['items']:
                        time.sleep(2)
                        vacancy = parser.get_vacancy_by_id(item['id'])
                        try:
                            print((lang, page, vacancy['id'],
                                   vacancy['name'],
                                   vacancy['employer']['name'],
                                   vacancy['employer']['accredited_it_employer'],
                                   vacancy['salary'],
                                   vacancy['experience']['name'],
                                   vacancy['area']['name'],
                                   vacancy['initial_created_at'],
                                   vacancy['key_skills']
                                   ))
                            csv_handler.save_file(keyword=lang, page=page, data=vacancy)
                        except:
                            print(vacancy, item['id'])
