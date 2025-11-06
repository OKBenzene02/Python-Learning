# available_parts = ["computer",
#                    "mouse",
#                    "key board",
#                    "desktop",
#                    "cpu",
#                    "hdmi cable",
#                    "ok ok", 1]
# #valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
# valid_choices = []
# for i in range(1, len(available_parts) + 1):
#     valid_choices.append(str(i))
# print(valid_choices)
# current_choices = "-"
# computer_parts = []
# while current_choices != "0":
#     if current_choices in valid_choices:
#         index = int(current_choices) - 1
#         chosen_part = available_parts[index]
#         if chosen_part in computer_parts:
#             print("Removing {}".format(current_choices))
#             computer_parts.remove(chosen_part)
#         else:
#             print("Adding {}".format(current_choices))
#             computer_parts.append(chosen_part)
#         print("your list contains {}".format(computer_parts))
#
#     else:
#         print("please add options from the list below:")
#         for number, part in enumerate(available_parts):
#             print("{}: {}".format(number + 1, part))
#
#     current_choices = input()
#
# print(computer_parts)

# items = "-"
# lists = []
# while items != "0":
#     if items in "1234":
#         print("adding {}".format(items))
#         if items == "1":
#             lists.append("tomato soup")
#         elif items == "2":
#             lists.append("onions")
#         elif items == "3":
#             lists.append("tomato's")
#         elif items == "4":
#             lists.append("cinnamon")
#
#     else:
#         print("Please add options from the lists below:")
#         print("1: tomato soup")
#         print("2: onions")
#         print("3: tomato's")
#         print("4: cinnamon")
#         print("0: Exit")
#
#     items = input()
#
# print(lists)

