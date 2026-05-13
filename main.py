# 7-masala:
class University:
    def __init__(self, name, students_count):
        self.name = name
        self.__students_count = students_count

    def get_students_count(self):
        return self.__students_count

    def set_students_count(self, new_count):
        self.__students_count = new_count


u1 = University('TATU', 12000)
print(u1.name)
print(u1.get_students_count())
u1.set_students_count(15000)
print(u1.get_students_count())
