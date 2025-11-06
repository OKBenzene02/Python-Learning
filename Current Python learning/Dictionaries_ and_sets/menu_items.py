# available_parts = {"1": "computer",
#                    "2": "monitor",
#                    "3": "keyboard",
#                    "4": "mouse",
#                    "5": "hdmi cable",
#                    "6": "dvd drive",
#                    }
#
# current_choice = None
# computer_parts = []
#
# while current_choice != '0':
#     if current_choice in available_parts:
#         chosen_part = available_parts[current_choice]
#         if chosen_part in computer_parts:
#             print(f"Removing {chosen_part}.")
#             computer_parts.remove(chosen_part)
#         else:
#             print(f"Adding {chosen_part}")
#             computer_parts.append(chosen_part)
#         print(f'Your cart now contains {computer_parts}')
#     else:
#         print('Please add items from the available list: ')
#         print('='*25)
#         for key, val in available_parts.items():
#             print(f"{key}: {val}")
#         print(f"Enter 0 to exit....")
#
#     current_choice = input('> ')

print(list(i for i in range(1, 5+1)).pop(3))