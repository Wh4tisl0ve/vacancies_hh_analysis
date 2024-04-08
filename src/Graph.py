import plotly
import json

import plotly.express as px
from app import analysis


def create_bar_count_employer():
    fig = px.bar(
        x=analysis.get_count_vacancy_by_employer()['index'].index.array,
        y=analysis.get_count_vacancy_by_employer()['index'].values,
        barmode="group",
        labels={'x': 'Название компании', 'y': 'Количество вакансий'}
    )
    fig.update_layout(dragmode=False)

    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json


def create_bar_count_city():
    fig = px.bar(
        x=analysis.get_count_vacancy_by_city().index.array,
        y=analysis.get_count_vacancy_by_city().values,
        barmode="group",
        labels={'x': 'Город', 'y': 'Количество вакансий'},
    )
    fig.update_layout(dragmode=False)

    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
