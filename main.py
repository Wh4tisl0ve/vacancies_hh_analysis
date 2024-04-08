import src.Analyzer

def main():
    dict_query = {'query': ['Java', 'C#', 'Python', 'JavaScript', 'C++', 'PHP',
                            'Frontend, Backend, Fullstack', 'DevOps'],
                  'city': [1, 2, 3, 4, 88, 66, 54, 104, 78, 99]}
    # парсинг данных
    # parser = src.Parser.Parser(dict_query)
    # parser.parsing()
    analyzer = src.Analyzer.Analyzer()
    print(analyzer.get_count_vacancy_by_city().sort_values(ascending=False))






if __name__ == "__main__":
    main()
