class Student:
    def __init__(self, name = "", midterm = 0, final = 0):
        self._name = name
        self._midterm = midterm
        self._final = final

    def setName(self, name):
        self._name = name
    def setMidterm(self, midterm):
        self._midterm = midterm
    def setFinal(self, final):
        self._final = final
    def getName(self):
        return self._name

    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()

class LGStudent(Student):
    def __init__(self, name = "", midterm = 0, final = 0):
        super().__init__(name, midterm, final)
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        else:
            return "F"

class PFStudent(Student):
    def __init__(self, name = "", midterm = 0, final = 0):
        super().__init__(name, midterm, final)
    def calcSemGrade(self):
        average = round((self._midterm + self._final) / 2)
        if average >= 60:
            return "Pass"
        else:
            return "Fail"
