"""FIRST EXAMPLE"""
# l = 10
# def func(n):
#     l = 20 # property of func(n)
#     print(l, "this is an example")
#
# func("ok lets see")

"""SECOND EXAMPLE"""
# l = 10
# def func(n):
#     l = l + 4 # This throws an error showing- local variable 'l' referenced before assignment
#     print(l, "this is an example")
#
# func("ok lets see")

"""SOLUTION FOR THIS"""
# l = 10
# def func(n):
#     global l
#     l = l + 4 # Output- 14 this is an example
#     print(l, "this is an example")
#
# func("ok lets see")
