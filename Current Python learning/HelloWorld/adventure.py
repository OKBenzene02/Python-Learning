available_exits = ["north", "south", "west", "east"]
choosen_exit = ""
while choosen_exit not in available_exits:
    choosen_exit = input("Please choose a direction: ").casefold()
    if choosen_exit.casefold() == "quit":
        print("Game over")


else:
    print("arent you glad to get out of here.")

