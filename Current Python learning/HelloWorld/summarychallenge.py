# choice = " "
# while choice != "0":
#
#     if choice in "12345" :
#         print("you chose {}.".format(choice))
#     else:
#         print("please choose your option from the list below:")
#         print("1. Learn python")
#         print("2. Learn java")
#         print("3. go swimming")
#         print("4. Have dinner")
#         print("5. Go to bed")
#         print("0. Exit")
#
#     choice = input()

choice = "-"
while choice != "0":

    if choice in "12345" :
        print("you can choose {}.".format(choice))

    else:
        print("Please choose your option from the list below:")
        print("1. learn python")
        print("2. learn java")
        print("3. go swimming")
        print("4. have dinner")
        print("5. go to bed")
        print("6. Exit")

    choice = input()