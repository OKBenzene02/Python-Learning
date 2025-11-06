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
# pep8 style guide.
for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)

    else:
        print("{} has a spam score of {}".format(meal, meal.count("spam")))
