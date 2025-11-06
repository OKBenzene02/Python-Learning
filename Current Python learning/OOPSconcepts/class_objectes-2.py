# class Students:
#     leaves = 4
#     def __init__(self, a_name, a_section):
#         self.name = a_name
#         self.section = a_section
#
#
#     def print_details(self):
#         return "Name is {}, section in {}".format(self.name, self.section)
#
#     @classmethod
#     def leave_change(cls, new_leave):
#         cls.leaves = new_leave
#
# # #liyakhat = Students("hello", 5) # I cannot do it because we have not yet constructed the Students class...
# liyakhat = Students("liyakhat", 13)
# # liyakhat.name = "liyakhat"
# # liyakhat.section = 13
# # liyakhat.leaves = 14
# # print(liyakhat.print_details())
# # print(liyakhat.name)
# # print(liyakhat.section)
# Students.leave_change(15)
# print(liyakhat.leaves)


# class StudentDetails:
#
#     def __init__(smtg, name, rrn, marks):
#         smtg.name = name
#         smtg.rrn = rrn
#         smtg.marks = marks
#
#     def details(smtg):
#         print(f"Name: {smtg.name}, RRN: {smtg.rrn}")
#
#     def marks_mere(smtg):
#         subjects = ["Maths", "Physics", "Computers"]
#         for i in range(0, 3):
#             print(f"{subjects[i]} = {smtg.marks[i]}")
#
#
# Mere_details = StudentDetails("liyakhat", 3249257, [24, 25, 26])
#
# Mere_details.details()
# Mere_details.marks_mere()
#
# class Employee:
#
#     def __init__(self, a_name, a_id, a_leaves):
#         self.name = a_name
#         self.id = a_id
#         self.leaves = a_leaves
#
#     def details(self):
#         return f"Name: {self.name} \nID: {self.id} \nNumber of Leaves: {self.leaves}"
#
#
# mere_employee = Employee("Liyakhat", 542523, 5)
# print(mere_employee.details())

# class Empty:
#     pass
#
# smtg = Empty()
# smtg.name = "Liyakhat"
# smtg.id = 8475182
# print(smtg.name)
# print(smtg.id)
# del smtg.name
# print(smtg.name)
#
# class Employee:
#     salary = 0
#
#
# mere_employee = Employee()
# mere_employee.salary = 5000
# # Adding new properties to Employee class.
# mere_employee.name = "Liyakhat yousuf mogal"
# mere_employee.age = 20
# print("Employee NAME: ", mere_employee.name)
# print("Employee AGE: ", mere_employee.age)
# print("Employee SALARY: ", mere_employee.salary)

# average = 0
# l = []
# while True:
#     num = int(input("Enter a number: "))
#     l.append(num)
#     if num == -1:
#         print(f"The average of entered numbers is: {sum(l[:-1]) / len(l[:-1])}")
#         break

# l = [1, 2, 3, 4, 5]
# print(l[:-1])

def add(a, b):
    return a + b

def printFunc(a, b, math):
    print(f'Sum of two numbers is {math(a, b)}')

printFunc(5, 3, add)