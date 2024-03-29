import requests
import datetime

from dateutil.relativedelta import relativedelta


# класс, позволяющий взаимодействовать с API hh.ru
class ApiHH:
    def __init__(self):
        # адрес запроса
        self.__url = f"https://api.hh.ru"

        # диапазон дат для вакансий
        self.__dt_from = (datetime.date.today() - relativedelta(years=1)).strftime('%Y-%m-%d')
        self.__dt_to = datetime.date.today().strftime('%Y-%m-%d')

    # получение параметров запроса
    def get_vacancies_params(self, text: str, city: str, page: int) -> dict:
        params = {
            "text": f'NAME:{text}',
            'date_from': self.__dt_from,
            'date_to': self.__dt_to,
            'currency': 'RUR',
            'clusters': True,
            'page': page,
            "area": city,
            "per_page": 100
        }

        return params

    def get_headers(self) -> dict:
        headers = {
            'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0",
        }
        return headers

    # получить результат запроса к API
    def get_vacancy_request(self, params, headers):
        ses = requests.Session()
        response = ses.get(url=f'{self.__url}/vacancies', params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data

    # получение полной информации о вакансии по id
    def get_vacancy_by_id(self, vacancy_id: int):
        ses = requests.Session()
        response = ses.get(url=f'{self.__url}/vacancies/{vacancy_id}')

        if response.status_code == 200:
            data = response.json()
            return data
