import time

import src.ApiHH
import src.FileHandler


# класс для парсинга вакансий
class Parser:
    def __init__(self):
        self.__api_hh = src.ApiHH.ApiHH()
        self.__csv_handler = src.FileHandler.CSVHandler()

    def parse_vacancy(self, dict_query: dict, cnt_page: int) -> None:
        # перебор списка ключевых слов
        for keyword in dict_query['query']:
            # перебор городов
            for city in dict_query['city']:
                # по страницам
                for page in range(0, cnt_page):
                    params = self.__api_hh.get_vacancies_params(text=keyword, city=city, page=page)
                    headers = self.__api_hh.get_headers()
                    data = self.__api_hh.get_vacancy_request(params, headers)
                    for item in data['items']:
                        time.sleep(2)
                        vacancy = self.__api_hh.get_vacancy_by_id(item['id'])
                        try:
                            self.__csv_handler.save_file(keyword=keyword, page=page, data=vacancy)
                        except Exception as exc:
                            raise exc
