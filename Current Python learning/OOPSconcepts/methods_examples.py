class Students:
    leaves = 4

    def __init__(self, a_name, a_section):
        self.name = a_name
        self.section = a_section

    def print_details(self):
        return "Name is {}, section in {}".format(self.name, self.section)

    @classmethod
    def leave_change(cls, new_leave):
        cls.leaves = new_leave

    @classmethod
    def spec(cls, string):
        parameters = string.split("-")
        return Students(parameters[0], parameters[1])


liyakhat = Students("liyakhat", 13)
liyakhat1 = Students.spec("liyakhat-13")
# Students.leave_change(15)
# print(liyakhat.leaves)
print(liyakhat1.section)