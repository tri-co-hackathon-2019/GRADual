from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(64))
    number = db.Column(db.Integer)
    term = db.Column(db.Integer) # 0 for Fall, 1 for Spring, 2 for every sem