# even = [2, 4, 6, 8, 0]
# odd = [1, 3, 5, 7, 9, 11]
# numbers = [even, odd]
# print(numbers)
# for number_list in numbers:
#     print(number_list)
#     for value in number_list:
#         print(value)

# numbers = [n for n in range(4)]
# print(numbers)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[3:]:
    print(player.title())