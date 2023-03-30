class Person:
  def __init__(self, student, prelim, midterm, final):
    self.student = student
    self.__prelim = prelim
    self.__midterm = midterm
    self.__final = final
  def Grade(self):
    return (self.__prelim * 0.3) + (self.__midterm * 0.3) + (self.__final * 0.4)
  def display(self):
   print(f"{self.student} grade for prelim is {self.__prelim}, for midterm is {self.__midterm}, and for finals is {self.__final} with an avererage grade of {self.Grade()}")

class std1(Person):
  def __init__(self):
    student = "Student 1"
    prelim = float(input(f"(Student1) Input the grade for prelim: "))
    midterm = float(input(f"(Student2) Input the grade for midterm: "))
    final = float(input(f"(Student3) Input the grade for final: "))
    super().__init__(student, prelim, midterm, final)
class std2(Person):
  def __init__(self):
    student = "Student 2"
    prelim = float(input(f"(Student1) Input the grade for prelim: "))
    midterm = float(input(f"(Student2) Input the grade for midterm: "))
    final = float(input(f"(Student3) Input the grade for final: "))
    super().__init__(student, prelim, midterm, final)
class std3(Person):
  def __init__(self):
    student = "Student 3"
    prelim = float(input(f"(Student1) Input the grade for prelim: "))
    midterm = float(input(f"(Student2) Input the grade for midterm: "))
    final = float(input(f"(Student3) Input the grade for final: "))
    super().__init__(student, prelim, midterm, final)

Std1 = std1()
Std2 = std2()
Std3 = std3()

Std1.display()
Std2.display()
Std3.display()