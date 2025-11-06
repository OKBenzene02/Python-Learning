# # Simple python temperature program
# print("\tTemperature conversion\t")
# print("""Scales available
#       ->Celsius
#       ->Fahrenheit
#       ->Kelvin""")
# temp = input("enter a temperature to convert: ")
# degree = int(temp[:-1]) # prints the value excluding units
# units = temp[-1]
#
# if units.upper() == 'C':
#     asking = input("conversion in \"F\" (or) \"K\": ")
#     if asking.upper() == "F":
#         result = int(round((9 * degree)/5 + 32))
#         print("{} == {}{}".format(temp, result, asking))
#     elif asking.upper() == "K":
#         result = int(round(degree + 273))
#         print("{} == {}{}".format(temp, result, asking))
# elif units.upper() == 'F':
#     asking = input("conversion in \"C\" (or) \"K\": ")
#     if asking.upper() == "C":
#         result = int(round(5/9 * (degree - 32)))
#         print("{} == {}{}".format(temp, result, asking))
#     elif asking.upper() == "K":
#         result = int(round((5/9 * (degree - 32)) + 273))
#         print("{} == {}{}".format(temp, result, asking))
# elif units.upper() == 'K':
#     asking = input("conversion in \"C\" (or) \"F\": ")
#     if asking.upper() == "C":
#         result = int(round(degree - 273))
#         print("{} == {}{}".format(temp, result, asking))
#     elif asking.upper() == "F":
#         result = int(round((9/5 * (degree - 273)) + 32))
#         print("{} == {}{}".format(temp, result, asking))
# else:
#     print("enter proper units.")
#     quit()

# # =======================================================

