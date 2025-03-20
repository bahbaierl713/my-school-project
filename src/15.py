import random
class SchoolProject(object):
    def __init__(self, name):
        self.name = name

    def get_grade(self):
        grades = [95, 87, 100, 92, 83, 78, 96, 85, 94, 82]
        return random.choice(grades)