# Dobble Game

import string
import random


string_list = list(string.ascii_letters)
# print(string_list)

card1 = [0] * 5
card2 = [0] * 5

pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)
print(pos1)
print(pos2)

same_symbol = random.choice(string_list)

string_list.remove(same_symbol)

if pos1 == pos2:
    card2[pos1] = same_symbol
    card1[pos1] = same_symbol
else:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol
    card1[pos2] = random.choice(string_list)
    string_list.remove(card1[pos2])
    card2[pos1] = random.choice(string_list)
    string_list.remove(card2[pos1])

i = 0

while i < 5:
    if i != pos1 and i != pos2:
        alpha1 = random.choice(string_list)
        string_list.remove(alpha1)
        alpha2 = random.choice(string_list)
        string_list.remove(alpha2)
        card1[i] = alpha1
        card2[i] = alpha2
    i += 1

print(card1)
print(card2)

ch = input("Choose a figure that is similar: ")
if ch == same_symbol:
    print("Correct!!!")
else:
    print("!!!Wrong")