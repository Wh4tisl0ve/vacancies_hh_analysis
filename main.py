import re
import requests
import pandas as pd
import csv


# получение вакансий по ключевому слову и городу
def get_vacancies_from_hh(keyword, city, page=1, year = 2024):
    ses = requests.Session()
    url = f"https://api.hh.ru/vacancies?clusters=true&only_with_salary=true"
    params = {
        "text": keyword,
        'page': page,
        "area": city,
        "per_page": 100,  # количество запрашиваемых вакансий,
        'created_at': f'{year}-01-01',
    }
    headers = {
        'HH-User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0",
    }

    response = ses.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
    return vacancies


def write_vacancies_to_csv(vacancies):
    with open('data.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for row in vacancies:
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


def get_areas():
    url = f"https://api.hh.ru/areas/113"
    headers = {
        "User-Agent": "User-Agent",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for i in data['areas']:
            print((i['id'], i['name'], i['areas']), end='\n')


def main():
    # настройки для полного вывода структур данных
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)

    # массив самых популярных языков
    most_popular_lang = ['Java', 'C#', 'Python', 'JavaScript', 'C++', 'PHP']

    # массив ID крупных городов в России
    # 1 - МСК, 2 - СПБ, 3 - ЕКБ, 4 - Новосибирск, 88 - Казань, 66 - НН,54 - Красноярск, 104 - Челябинск, 78 - Самара, 99 - Уфа
    most_popular_city = [1, 2, 3, 4, 88, 66, 54, 104, 78, 99]

    # массив годов
    last_five_years = [2024, 2023, 2022, 2021, 2020]

    for i in most_popular_lang:
        for j in most_popular_city:
            for k in range(1, 3):
                data = get_vacancies_from_hh(i, j, k, last_five_years[4])
                write_vacancies_to_csv(data)
    # df = pd.read_csv("data.csv", encoding='windows-1251')
    # print(df)


if __name__ == "__main__":
    main()
