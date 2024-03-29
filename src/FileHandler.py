import csv
from abc import ABC, abstractmethod


# абстрактный класс для обработки файлов
class AbstractFileHandler(ABC):
    @abstractmethod
    def save_file(self, keyword, page, data):
        pass

    @abstractmethod
    def read_file(self):
        pass


# класс по работе с CSV файлами
class CSVHandler(AbstractFileHandler):
    def save_file(self, keyword: str, page: int, data: dict) -> None:
        with open('data.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            try:
                csvwriter.writerow((keyword, page, data['id'], data['name'], data['employer']['name'],
                                    data['employer']['accredited_it_employer'], data['salary'],
                                    data['experience']['name'], data['area']['name'],
                                    data['initial_created_at'], data['key_skills']
                                    ))
            except Exception as exc:
                raise exc

    def read_file(self):
        pass
