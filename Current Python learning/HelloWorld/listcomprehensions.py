# results = []
# for outer_loop_variable in outer_sequence:
#     for inner_loop_variable in inner_sequence:
#         results.append( expression_involving_loop_variables )

"""
The above is an example syntax for- for loop involving list comprehension.
"""
# results = []
# for x in [1, 2, 3]:
#     for y in [4, 5, 6]:
#         results.append([x, y])
#
# print(results)         # This is an sample example for list generation

# print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])   # this is an example of list comprehensions
# # =============================================================================
# x = int(input("X: "))
# y = int(input("y: "))
# z = int(input("z: "))
# n = int(input("n: "))
# res = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
# print(res)
# # =============================================================================
