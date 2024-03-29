import time
from statistics import mean

import numpy as np
import pandas as pd

import src.Analyzer


def main():
    dict_query = {'query': ['Java', 'C#', 'Python', 'JavaScript', 'C++', 'PHP',
                            'Frontend, Backend, Fullstack', 'DevOps'],
                  'city': [1, 2, 3, 4, 88, 66, 54, 104, 78, 99]}
    # парсинг данных
    # parser = src.Parser.Parser(dict_query)
    # parser.parsing()
    analyzer = src.Analyzer.Analyzer()
    print(analyzer.get_popular_skills())


if __name__ == "__main__":
    main()
