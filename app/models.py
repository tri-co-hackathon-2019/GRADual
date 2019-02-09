from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(64))
    number = db.Column(db.Integer)
    term = db.Column(db.String(5)) # F for Fall, S for Spring, E for every sem
    frequency = db.Column(db.Integer)
    taken = db.Column(db.Boolean)
    core = db.Column(db.Boolean)
    domain = db.Column(db.String(5))
    parent = db.Column(db.Integer)

    def __repr__(self):
        return "{}{}, Prereq: {}".format(self.department, self.number, self.parent)

        #     self.department = department
        # self.number = number
        # self.term = term
        # self.frequency = frequency
        # self.taken = taken
        # self.core = core
        # self.domain = domain
