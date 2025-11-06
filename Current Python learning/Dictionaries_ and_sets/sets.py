# set_things = {"you", "i", "people", "states"}
# print(set_things)
# for things in set_things:
#     print(things)
#
# # similar example
# things_of_sets = set(["jam", "vanilla", "cream", "chocolate"])
# print(things_of_sets)
#
# for thing in things_of_sets:
#     print(thing)
# set_things.add("horse")
# things_of_sets.add("horse")
# print(set_things)
# print(things_of_sets)

# empty_set = set()
# empty_set2 = {}
# empty_set.add("ok")
# # empty_set2.add("it is added")
#
# set_numbers = set(range(21))
# print(set_numbers)
#
# set1 = set(range(0, 21, 2))
# print(len(set1))
#
# print(len(set_numbers.union(set1)))
# print(set_numbers.union(set1))
#
# print(set_numbers.intersection(set1))
# # print(set1.intersection(set_numbers))
# # print(len(empty_set.intersection(set1)))

# even = set(range(0, 31, 2))
# print(sorted(even))
# tuple_square = (4, 9, 16, 25)
# square = set(tuple_square)
# print(sorted(square))
#
# print("even minus squares")
# print(sorted(even.difference(square)))
# print(sorted(even - square))
#
# print(square.difference(even))
# print(square - even)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# tuple_squares = (1, 4, 9, 16, 25)
# squares = set(tuple_squares)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(even.union(tuple_squares))
#
# print("-" * 20)
# print(even & squares)
# print(squares.intersection(squares))
# print(sorted(squares))

# even = set(range(0, 20, 2))
# # print(even)
# print(sorted(even))
# print(len(sorted(even)))
#
# squares_tuple = (1, 4, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
# print(len(sorted(squares)))

# print(even - squares)
# print(even.difference(squares))
# print(squares.difference(even))
#
# print("=" * 40)
# print(sorted(even))
# even.difference_update(squares)
# print(sorted(even))
#
# print("symmetric even minus squares.")
# even.symmetric_difference(squares)
# print(even)
# squares.symmetric_difference(even)
# print(squares)
#
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
#
# try:
#     squares.remove(8)
# except KeyError:
#     print("The number 8 is not a member of the group.")


even = set(range(0, 20, 2))
# print(even)
# print(sorted(even))
# print(len(sorted(even)))

squares_tuple = (4, 16)
squares = set(squares_tuple)
# print(sorted(squares))
# print(len(sorted(squares)))

if squares.issubset(even):
    print("squares is the subset of even.")
if squares.issuperset(even):
    print("squares is the subset of even.")



