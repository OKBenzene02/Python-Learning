# shopping_list = ["milk", "soap", "eggs", "bread", "spam", "rice"]
# # for items in shopping_list:
# #     if items != "spam":
# #         print("buy " + items)
# item_to_find = "okok"
# found_at = None
#
# # for index in range(len(shopping_list)):
# #     if shopping_list[index] == item_to_find:
# #         found_at = index
# #         break
#
# if item_to_find in shopping_list:
#     found_at = shopping_list.index(item_to_find)
#
# if found_at is not None:
#     print("item found at position {}".format(found_at))
# else:
#     print("item {} not found".format(item_to_find))

lists = ["pen", "eraser", "marker", "cutter", "sketches"]
to_find = input("Please enter an item to search: ").casefold()
found_at = None
if to_find in lists:
    found_at = lists.index(to_find)
if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("sorry no item with name {}".format(to_find))