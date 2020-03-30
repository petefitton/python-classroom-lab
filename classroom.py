class Assignment():
    def __init__(self, name, github_url):
        self.name = name
        self.github_url = github_url
        self.completed = False
        self.grade = None

    def mark_done(self, grade):
        self.grade = grade
        self.completed = True

class Student():
    def __init__(self, name):
        self.name = name
        self.pending_homeworks = []
        self.completed_homeworks = []
    
    # Assignment does not have to be capitalized
    def assign_homework(self, Assignment):
        self.pending_homeworks.append(Assignment)

    def complete_homework(self, name, grade):
        # find the specific homework in pending_works list and call its mark_done() method
        # find Assignment that has the same name as the argument name
        # method should remove the Assignment from pending_works and add it to completed_homeworks
        for assignment in self.pending_homeworks:
            if assignment.name == name:
                assignment.mark_done(grade)
                self.pending_homeworks.remove(assignment)
                self.completed_homeworks.append(assignment)

        # alternative way to code the above:
        # for index in range(0, len(self.pending_homeworks)):
        #     if (name == self.pending_homeworks[index].name):
        #         assignment = self.pending_homeworks.pop(index)
        #         assignment.mark_done(grade)
        #         self.completed_homeworks.append(assignment)
        #         return True

    def print_outstanding_homeworks(self):
        temp = []
        for homework in self.pending_homeworks:
            temp.append(homework)
        try:
            temp[0]
            print(f"{self.name} needs to turn in: {temp[0]}")
        except IndexError:
            print(f"{self.name} has no outstanding homeworks!")

        # alternative way to do the above
        # if (len(self.pending_homeworks) <= 0):
        #     print(str(self.name) + " has no outstanding homeworks.")
        # else:
        #     for homework in self.pending_homeworks:
        #         print(str(self.name) + " needs to complete " + str(homework.name))


class SeiClass():
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, Student):
        self.students.append(Student)

    def assign_homework(self, Assignment):
        # assign Assignment to all students in this SeiClass
        for student in self.students:
            student.assign_homework(Assignment)


henry = Student('Henry')
sarah = Student('Sarah')
mike = Student('Mike')
print(f"""Student:
    Name: {henry.name}
    Pending: {henry.pending_homeworks}
    Completed: {henry.completed_homeworks}""")

sei26 = SeiClass('sei26')
sei26.add_student(henry)
sei26.add_student(sarah)
sei26.add_student(mike)


assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')
print(f"""Assignment 1: 
    Name: {assignment1.name} 
    Url: {assignment1.github_url} 
    Completed: {assignment1.completed} 
    Grade: {assignment1.grade}""")

print("Assigned a homework to the class")
sei26.assign_homework(assignment1)
print(f"""Student:
    Name: {henry.name}
    Pending: {henry.pending_homeworks}
    Completed: {henry.completed_homeworks}""")
print(f"""Student:
    Name: {sarah.name}
    Pending: {sarah.pending_homeworks}
    Completed: {sarah.completed_homeworks}""")

henry.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

henry.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
mike.print_outstanding_homeworks()