fruit = {"orange": "a sweet orange, citrus fruit",
         "apple":  "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": 'a small sweet fruit growing in bunches',
         "lime": "a sour green citrus fruit"}

veg = {"cabbage": "healthy for all",
       "sprouts": "very healthy seeds",
       "spinach": 'helps you grow tall'}

okok = veg.copy()
okok.update(fruit)
print(okok)

# veg.update(fruit)
# print(veg)





# print(fruit)
# print(fruit["grape"])
# print(fruit["lemon"])
# # adding dictionaries
# fruit["pear"] = "its an odd shaped apple"
# print(fruit)
# # over writing, the added dictionaries or the current dictionaries
# fruit["pear"] = "overwriting the dictionary"
# print(fruit)
# # for an empty dictionary
# fruit.clear()
# print(fruit)
# while True:
#     fruit_get = input("Please enter a fruit: ").casefold()
#     if fruit_get == "quit":
#         break
#
#     key_get = fruit.get(fruit_get, "we don't have " + fruit_get)
#     print(key_get)
#     # if fruit_get in fruit:
#     #     key_get = fruit.get(fruit_get)
#     #     print(key_get)
#     # else:
#     #     print("we dont have a", fruit_get)

# # checking whether dictionaries change
# for i in range(11):
#     for snack in fruit:
#         print(snack, "is", fruit[snack])
#     print("=" * 50)

# # for sorting the dictionary
# ordered_dict = list(fruit.keys())
# ordered_dict.sort()
# print(ordered_dict)
#
# for i in ordered_dict:
#     print(i, " == " + fruit[i])

# fruit_sorted = sorted(list(fruit.keys()))
# for i in fruit_sorted:
#     print(i, " == " + fruit[i])