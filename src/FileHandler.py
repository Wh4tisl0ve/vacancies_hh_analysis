import csv
from abc import ABC, abstractmethod


# абстрактный класс для обработки файлов
class AbstractFileHandler(ABC):
    @abstractmethod
    def save_file(self, data):
        pass

    @abstractmethod
    def read_file(self):
        pass


# класс по работе с CSV файлами
class CSVHandler(AbstractFileHandler):
    def save_file(self, data):
        with open('../data.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            try:
                csvwriter.writerow((data['id'],
                                    data['name'],
                                    data['area']['name'],
                                    data['employer']['name'],
                                    data['salary'],
                                    data['snippet']['requirement'],
                                    data['experience']['name']))
            except:
                pass

    def read_file(self):
        pass
