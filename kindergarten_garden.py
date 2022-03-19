STUDENTS = [
    "Alice", "Bob", "Charlie", "David","Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
    ]
    
PLANTS = {
    "V": "Violets", 
    "R": "Radishes", 
    "C": "Clover", 
    "G": "Grass"
}

class Garden:
    def __init__(self, diagram, students = STUDENTS):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)
        
    def plants(self, student):
        index = self.students.index(student) * 2
        return [PLANTS[row[i]] for row in self.diagram for i in (index, index+1)]
