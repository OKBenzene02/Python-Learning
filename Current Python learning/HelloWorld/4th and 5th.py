# # ===========================================================
# ASCII to Characters and Characters to ASCII

# # Characters to ascii
# def index(a: str):
#       i = 0
#       for i in range(len(character)):
#             if a == character[i]:
#                   break
#       return i
#
# character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
# charEnter = input("Enter the character to convert to ascii number: ")
#
# if (charEnter == 'A'):
#       print(f"{charEnter} ascii value is 65.")
# else:
#       print(f"{charEnter} ascii value is {65 + index(charEnter)}")

# # Ascii to characters
# character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
# AsciiValue = int(input("Enter the number to convert in the ascii character: "))
#
# index = 65
# if AsciiValue == 65:
#     print(f"{AsciiValue} ascii character is A.")
#
# else:
#     index = AsciiValue - 65
#     print(f"{AsciiValue} ascii character is {character[index]}")

# # ===========================================================
#  Bit Stuffing and De-stuffing

# Bit stuffing
# bit = '111111001'
# bitList = list(bit)
#
# i = 0
# count = 0
#
# while i < len(bit):
#     if bitList[i] == '1':
#         count += 1
#     else:
#         count = 0
#     if count == 6:
#         bitList.insert(i, '0')
#         count = 0
#     i += 1
#
# print(bit)
# print("".join(bitList))

# Bit De-stuffing
# bit = "101011111001"
# bitLst = list(bit)
# i = 0
# count = 0
#
# while i < len(bitLst):
#     if bitLst[i] == '1':
#         count += 1
#     else: count = 0
#
#     if count == 5:
#         bitLst.__delitem__(i+1)
#         count = 0
#
#     i += 1
#
# print(bit)
# print("".join(bitLst))

# +, -, *, //, /, %, **
# print(12 % 2, 'remainder')
# print(12 // 2, 'quotient')
# print(12 / 2, 'divisor')
#
# pi = 3.14
# r = 12
# area = pi * (r ** 2)
# print(area)

# name = str(input("enter your name: "))
# age = int(input('enter your age: '))
# print(name, age)
#
# if age % 2 == 0:
#     print('even')
# else:
#     print("odd")

# x, y, z = input("enter three numbers: ").split()
# print(int(x), int(y), int(z))

# num = int(input('enter the number: '))
#
# if num % 2 != 0:
#     print('Weird')
#
# elif (num % 2 == 0) and (2 <= num <= 5):
#     print("Not Weird")
#
# elif (num % 2 == 0) and (6 <= num <= 20):
#     print("Weird")
#
# elif (num % 2 == 0) and (num > 20):
#     print("Not Weird")

l = list(i+1 for i in range(10))

print(l[0:4])
print(l[2:])
print(l[::])
print(l[1:5:2])
print(l[1:10:2])
print(l[::-1])
print(l[:-1])
print(l[-3:])