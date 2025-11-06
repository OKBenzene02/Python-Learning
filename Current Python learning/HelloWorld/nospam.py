menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]
# method 1
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(", ".join(meal))


# # method 2
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=" ")
#     print()
# ## gen code for method 2
# for meal in menu:
#     items = ", ".join((item for item in meal if item != 'spam'))
#     print(items)