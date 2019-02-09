class Course:
    def __init__(self, department, number, term, frequency,
                        taken, core, domain):
        
        self.department = department
        self.number = number
        self.term = term
        self.frequency = frequency
        self.taken = taken
        self.core = core
        self.domain = domain
    
    def __repr__(self):
        return "{}{} ({})".format(self.department,
                                self.number,
                                self.domain)