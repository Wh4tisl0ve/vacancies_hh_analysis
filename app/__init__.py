from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.Analyzer import Analyzer

app = Flask(__name__)
# конфигурация БД
app.config.from_object(Config)

# работа с бд
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# класс для анализа данынх
analysis = Analyzer()
data_frame_vacancies = analysis.get_df_vacancy()

from app import views
