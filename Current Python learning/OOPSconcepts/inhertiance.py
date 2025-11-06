"""SINGLE INHERITANCE"""
# class A:
#     def smtg(self):
#         print("ok- Class A")
# class B(A):
#     def smtg2(self):
#         print("ok- class B")
#
#
# w = B()
# w.smtg()
# w.smtg2()

# # =====================================

class Details:
    def __init__(self, aname, aid):
        self.name = aname
        self.id = aid

# class Student(Details):
#     def details(self):
#         print(f"Name- {self.name}\n"
#               f"id - {self.id}")
#
#
# d = Student("Liyakhat", 3561384)
# d.details()

# # =====================================
"""MULTI LEVEL INHERITANCE"""
# class Animal:
#     def speaking(self):
#         print("Speaking")
# class Dog(Animal):
#     def barking(self):
#         print("Barking")
# class DogChild(Dog):
#     def eating(self):
#         print("Eating")
#
#
# w = DogChild()
# w.eating()
# w.barking()
# w.speaking()
# # =====================================
"""MULTIPLE INHERITANCE"""
# class A:
#     print("OK -- class A")
# class B:
#     print("OK -- class B")
# class C(A, B):
#     print("ok -- class C")
#
# C()

"""Super() method"""
# class A:
#     def __init__(self, name):
#         print(name, "class A ka name")
# class B(A):
#     def __init__(self):
#         print("class B")
#         super().__init__("ok")
#
# a = B()

class A:
    def __init__(self, name):
        print(name, "class A ka name")

    def nameIt(self, *a):
        return a[1:20] if len(a) > 1 else a

class B(A):
    def __init__(self):
        print("class B")
        # super().__init__("ok")
        super().nameIt()

    def printUpperClass(self, *a):
        return self.nameIt(*a)

a = B()
a.printUpperClass(1,2,3,4,4,5234,1,33,324,2,3234)

# class addition:
#     def __init__(self,a=0,b=0):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return "({0},{1})".format(self.a,self.b)
#     def __add__(self,other):
#         a=self.a + other.a
#         b=self.b + other.b
#         return addition(a,b)
#
# obj = addition(1,2)
# obj1 = addition(3,4)
# print(obj+obj1)



