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
    csv_handler = src.FileHandler.CSVHandler()

    for lang in most_popular_lang:
        for city in most_popular_city:
            for page in range(0, 5):
                params = parser.get_vacancies_params(text=lang, city=city, page=page)
                headers = parser.get_headers()
                data = parser.get_vacancy_request(params, headers)
                if data is not None:
                    for item in data['items']:
                        vacancy = parser.get_vacancy_by_id(item['id'], params, headers)
                        if vacancy is not None:
                            print((vacancy['id'],
                                   vacancy['name'],
                                   vacancy['salary'],
                                   vacancy['area']['name'],
                                   vacancy['initial_created_at'],
                                   vacancy['employer']['name'],
                                   vacancy['key_skills']
                                   ))
                            print('-' * 50)
                        # csv_handler.save_file(item)
                else:
                    break



if __name__ == "__main__":
    main()
