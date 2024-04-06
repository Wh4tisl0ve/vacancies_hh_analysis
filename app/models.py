from app import db


class Vacancies(db.Model):
    keyword = db.Column(db.String(100), nullable=False)
    page = db.Column(db.Integer, nullable=False)
    id_vacancy = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employer = db.Column(db.String(100), nullable=False)
    accredited_it = db.Column(db.Boolean, nullable=False)
    salary = db.Column(db.String(200))
    experience = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    created_vacancy = db.Column(db.DateTime, nullable=False)
    skills = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Vacancy: {}>'.format(self.id_vacancy)

