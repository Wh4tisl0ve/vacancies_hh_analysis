from flask import render_template
from flask_paginate import Pagination, get_page_args
from app import app, data_frame_vacancies


# обработчики, для ответа на запросы браузера

@app.route("/")
def main():
    vacancies = data_frame_vacancies[['keyword', 'id_vacancy', 'name', 'employer', 'accredited_it',
                                      'experience', 'city', 'skillsRes', 'salaryRes']].rename(
        columns={'keyword': 'Ключевое слово', 'id_vacancy': 'ID', 'name': 'Должность',
                 'employer': 'Работодатель', 'accredited_it': "ИТ-аккредитация", 'experience': 'Опыт',
                 'city': 'Город', 'skillsRes': 'Навыки', 'salaryRes': 'Зарплата'})

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(vacancies)
    pagination_vacancy = vacancies[offset: offset + per_page]

    pagination = Pagination(page=page,
                            per_page=per_page,
                            total=total,
                            css_framework='bootstrap5')

    return render_template('index.html',
                           data=[pagination_vacancy.to_html(classes='table table-bordered table-sm')],
                           titles=vacancies.columns.values,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/parsing")
def parsing():
    return 'Здесь будет парсер с полем для ключевого слова, ввода количества страниц парсинга'


@app.route("/analysis")
def analysis():
    return 'Здесь будет вывод различных графиков с выводом таблицы данных'


@app.route("/about_project")
def about():
    return 'Здесь будет информация об авторе, целях проекта, результатах'
