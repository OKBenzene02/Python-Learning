locations = {0: "you are sitting in the home learning python",
             1: "you are on the road",
             2: "you are at the top of the hill",
             3: "you are in the building to seek in some rest",
             4: "you are in the valley ",
             5: "you are now in the forest and that's the dead end"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 5, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]
loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "

    print(locations[loc])

    if loc == 0:
        break

    direction = input("available exits are:" + availableExits + " ").upper()
    print()

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you cannot go in that direction.")




# mylist = ["a", "b", "c", "d"]
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "123456789"
# newstring = ""
# for i in letters:
#     newstring = "-mississippi ".join(numbers)
#
# print(newstring)