bike = {"make": "Honda",
        "model": "250 dream",
        "colour": "red",
        "engine size": 250}

details = input("please enter any detail of the bike to search: ")

selection = bike.get(details)
print(selection)




