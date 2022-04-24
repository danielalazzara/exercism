from collections import defaultdict


class School:
    def __init__(self):
        self.student = defaultdict(list)
        self.record = []
    
    def _is_student(self, name):
        for grade in self.student.keys():
            if name in self.student[grade]:
                return True

    def add_student(self, name, grade):
        if not self._is_student(name):
            self.student[grade].append(name)
            self.record.append(True)
        else:
            self.record.append(False)

    def roster(self):
        st = []
        for key in sorted(self.student.keys()):
            st += self.grade(key)
        return st

    def grade(self, grade_number):
        return sorted(self.student[grade_number])

    def added(self):
        return self.record
