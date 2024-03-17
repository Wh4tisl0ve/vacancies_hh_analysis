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
            for row in data:
                try:
                    csvwriter.writerow((row['id'],
                                        row['name'],
                                        row['area']['name'],
                                        row['employer']['name'],
                                        row['salary'],
                                        row['snippet']['requirement'],
                                        row['experience']['name']))
                except:
                    print('Ошибка записи строки')

    def read_file(self):
        pass
