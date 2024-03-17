import src.Parser
import src.FileHandler


def main():
    # настройки для полного вывода структур данных
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_colwidth', None)

    # массив самых популярных языков
    most_popular_lang = ['Java', 'C#', 'Python', 'JavaScript', 'C++', 'PHP']

    # массив ID крупных городов в России
    # 1 - МСК, 2 - СПБ, 3 - ЕКБ, 4 - Новосибирск, 88 - Казань, 66 - НН,54 - Красноярск, 104 - Челябинск, 78 - Самара, 99 - Уфа
    most_popular_city = [1, 2, 3, 4, 88, 66, 54, 104, 78, 99]

    parser = src.Parser.Parser()

    params = parser.get_vacancies_params(text=most_popular_lang[0], city=most_popular_city[0], page=1)
    headers = parser.get_headers()
    data = parser.get_vacancy_request(params, headers)

    for i in data['items']:
        print(i['id'], '|',
              i['name'], '|',
              i['area']['name'], '|',
              i['salary'], '|',
              i['employer']['name'], '|',
              i['experience']['name'], '|',
              i['snippet']['requirement'])


if __name__ == "__main__":
    main()
