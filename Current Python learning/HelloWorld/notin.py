# activity = input("what would you like to do today? ")
#
# if " cinema" not in activity.casefold():
#     print("But i want to go to the cinema")

# IF challenge

name = input("please enter your name: ")
age = int(input("please enter your age: "))
if 18 < age < 31:
    print("Enjoy your holiday")
else:
    print("Sorry, {} you are not allowed because you are {}.".format(name, age))