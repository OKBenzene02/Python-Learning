# number = input("Please enter any numbers, using separators you like: ")
# separators = ""
#
# for char in number:
#     if not char.isnumeric():
#         separators += char
#
# print(separators)
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print(sum([int(val) for val in values]))


# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us,123,5737,4164,464687?
# """
#
# # Use a for loop and an if statement to print just the capitals in the quote above.
# for char in quote:
#     if char.isnumeric():
#         print(char)


# extract = """Hello i am 1,lets extract something interesting so that
# ,We are able 2 understand the String Methods in python easily,
# lets go press 2, 4, 5.?!@#$$^^&
# """
# for char in extract:
#     if char.isupper():
#         print(char)
#
# for char in extract:
#     if char.islower():
#         print(char)
#
# for char in extract:
#     if char.isnumeric():
#         print(char)

