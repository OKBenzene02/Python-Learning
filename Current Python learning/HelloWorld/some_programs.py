# # ---- ARMSTRONG NUMBER ----
# number = int(input("Enter a number to check: "))
# temp = number
# sum_1 = 0
#
# while temp > 0:
#     remainder = temp % 10
#     sum_1 += remainder**3
#     temp //= 10
#
# if sum_1 == number:
#     print("{} is an armstrong number.".format(number))
# else:
#     print("{} is not an armstrong number.".format(number))

# # using functions
# def armstrong_number(num):
#     temp = num
#     sum_num = 0
#     while temp > 0:
#         remainder = temp % 10
#         sum_num += remainder**3
#         temp //= 10
#     if sum_num == num:
#         print("{} is an armstrong number.".format(num))
#     else:
#         print("{} is not an armstrong number.".format(num))
#
#
# one_number = int(input("Enter a number: "))
# armstrong_number(one_number)

# # ==========================================================

# # ---- PATTERN USING NUMBERS ----
# rows = int(input("Enter number of Row's:  "))
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()
# # ---- ALTERNATE WAY ----
# row = 5
# for j in range(1, row + 1):
#     print("*" * j)

# # ==========================================================

# # ---- PATTERN USING STARS ----
# n = int(input("Enter number of Row's :"))
# for row in range(n):
#     for column in range(n):
#         if (column == 0) or (row == (n-1)) or (row == column):
#             print("*", end=' ')
#         else:
#             print(end="  ")
#     print()

# # ==========================================================
# # ---- PATTERN USING NUMBERS in -90 degrees ----
# rows = int(input("Enter number of Row's:  "))
# for i in range(rows + 1, 0, -1):
#     for j in range(i, 0, -1):
#         print(i, end=" ")
#     print()
# # ==========================================================

# n = int(input("enter number of lines: "))
# bool_input = int(input("enter 1 or 0: "))
#
# if bool_input == 1:
#
#     for i in range(1, n):
#         for j in range(0, i):
#             print("*", end=" ")
#         print()
#
# elif bool_input == 0:
#
#     for i in range(n, 0, -1):
#         for j in range(i, 0, -1):
#             print("*", end=" ")
#         print()
#
# if bool_input != 0 and bool_input != 1:
#     print("plz enter in 0 and 1: ")

# class Stars:
#
#     def right_up(self, n):
#         for i in range(1, n + 1):
#             for j in range(0, i):
#                 print("*", end=" ")
#             print()
#
#     def right_down(self, n):
#         for i in range(n, 0,  -1):
#             for j in range(i, 0, -1):
#                 print("*", end=" ")
#             print()
#
# row = int(input("enter number of row's: "))
# bool_val = int(input("0 or 1: "))
# a = Stars()
# if bool_val == 0:
#     print(a.right_up(row))
# elif bool_val == 1:
#     print(a.right_down(row))

# # ==========================================================

# # ----- FACTORIAL PROGRAM -----
# def fact(n) -> int:
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# number = int(input("enter a number: "))
# res = fact(number)
# print("{}! = {}".format(number, res))

# # ---- FACTORIAL USING LOOPS ----
# number = int(input("Enter a number: "))
# result = 1
# if number == 0 or number == 1:
#     print("{}! = 1".format(number))
# else:
#     for i in range(number, 0, -1):
#         result *= i
#     print("{}! = {}".format(number, result))

# # -----FACTORIAL-----

# num = int(input("Enter a number: "))
# if (num == 0) or (num == 1):
#     print("{}! = 1".format(num))
# else:
#     after_1 = 2
#     for i in range(3, num + 1):
#         after_1 *= i
#     print("{}! = {}".format(num, after_1))
# # -----FACTORIAL-----

# def fact(n: int) -> int:
#     if (n == 0) or (n == 1):
#         return 1
#     else:
#         after_1 = 2
#         for i in range(3, n + 1):
#             after_1 *= i
#         return after_1
#
#
# num = int(input("Enter a number: "))
# print("{}! = {}".format(num, fact(num)))
# -----FACTORIAL USING RECURSION-----
# def fact(n: int) -> int:
#     if (n == 0) or (n == 1):
#         return 1
#     else:
#         return n*fact(n - 1)
#
#
# num = int(input("Enter a number: "))
# print("{}! = {}".format(num, fact(num)))

# # =======================================================
# # ---- REVERSE A STRING ----
# iostr = str(input("enter a string: "))
# reverse = ""
# for i in iostr:
#     reverse = i + reverse
# print(reverse)

# # ---- USING FUNCTIONS ----
# def reversestr(stringio) -> str:
#     reverse = ""
#     for i in stringio:
#         reverse = i + reverse
#     print(reverse)
#
#
# stringgiven = str(input("enter a string: "))
# print("Before: ", stringgiven)
# print("After: ")
# reversestr(stringgiven)
# ----- SWAP CASE ----
# def swap_case(s):
#     empty = ""
#     for i in s:
#         if i.islower():
#             i = i.upper()
#         else:
#             i = i.lower()
#         empty += "".join(i)
#     return empty
#
# if __name__ == '__main__':
#     s = input("enter a string: ")
#     print(swap_case(s))


# # =========================================================

# # ---- FIBONACCI SERIES ----
# num1, num2 = 1, 0
# print(0, num2)
# print(1, num1)
#
# for i in range(2, 21):
#     temp = num1 + num2
#     num2 = num1
#     num1 = temp
#     print(i, temp)

# #---- USING FUNCTIONS ----
# def fibbo(n: int):
#     zero, one = 0, 1
#
#     temp = 0
#     for i in range(n - 1):
#         temp = one + zero
#         zero = one
#         one = temp
#     return temp
#
#
# for i in range(21):
#     print(i, fibbo(i))

# # ---- FIBONACCI SERIES USING RECURSION -----
# def fibbo(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibbo(n -1) + fibbo(n - 2))
#
#
# terms = int(input("Enter the range: "))
# if terms < 0:
#     print("Enter positive range.")
# else:
#     print("Fibonacci series")
#     for i in range(terms + 1):
#         print(i, fibbo(i))

# # ==========================================================
# # ---- POSITIVE NUMBERS ADDITION ----
# sum1 = 0
# numbers = int(input("Number of numbers to be added: "))
# for i in range(numbers):
#     positive = int(input("enter numbers: "))
#     if positive < 0:
#         continue
#     sum1 += positive
# print("TOTAL: ", sum1)
# # ===========================================================
# # ---- FLOYD'S TRIANGLE -----
# rows = int(input("enter number of rows: "))
# n = 1
# for i in range(1, rows):
#     for j in range(1, i + 1):
#         print(n, end=" ")
#         n += 1
#     print()
# # ===========================================================
# # ---- STRING IN TRIANGLE ----
# string = input("enter a word: ")
# row = len(string) # To avoid errors
# for i in range(1, row + 1):
#     for j in range(1, i + 1):
#         print(string[j], end="")
#     print()
#
# # ==========================================================
# # ---- PRIME NUMBER'S ----
# ---> IN EXPECTED RANGE
# for i in range(1, 21):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# # ----> IN GIVEN RANGE
# lower = int(input("enter lower range: "))
# higher = int(input("enter higher range: "))
# num = 1
# for num in range(lower, higher + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
# # ----- USING FUNCTIONS PRIME NUMBER -----
# def prime(n):
#     for i in range(n):
#         if i > 0:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 print(i)
#
#
# high = int(input("enter range: "))
# print(prime(high))
# # =======================================================
# # ---- SQUARE ROOT ---- (Using newton Raphson)
# def squareroot(n):
#     temp = n
#     if n > 0:
#         for i in range(n + 1, -1, -1):
#             n = (n + temp/n) / 2
#     else:
#         n = -0.000001
#     return n
#
#
# number = int(input("enter a number: "))
# res = squareroot(number)
# print("square root of {} = {:.3f}".format(number, res))

# def sqrt(x: int):
#     l, r = 0, x
#     while l <= r:
#         mid = (l + r) // 2
#         if (mid * mid) <= x < ((mid + 1) * (mid + 1)):
#             return mid
#         if x < (mid * mid):
#             r = mid - 1
#         else:
#             l = mid + 1
#
# print(sqrt(15))

# # =======================================================
# # ----- RANDOM NUMBER GENERATOR (3-DIGIT) -----
# import random
# highest = 10
# number1 = random.randint(0, highest)
# strnum1 = str(number1)
# number2 = random.randint(0, highest)
# strnum2 = str(number2)
# number3 = random.randint(0, highest)
# strnum3 = str(number3)
#
# random_number = strnum1 + strnum2 + strnum3
# print("Random 3-digit number:", random_number)

# # =======================================================
# ---- SUM OF NATURAL NUMBERS ----
# number = int(input("Enter a number range: "))
# adding = 0
# if number < 0:
#     print("Enter a positive number.")
#
# else:
#     while(number > 0):
#         adding += number
#         number -= 1
#     print("SUM:", adding)
# # =======================================================
# # # ---- SUM OF EVEN ODD IN A RANGE ----
# def sum_eo(n: int, t: str):
#     """
#
#     :param n: Used in defining a specific range
#     :param t: e: even, o: odd are the two strings used
#     :return: if the user enters the range as 10
#     we need him/her to get an input if those numbers are to be even or odd
#     then we start with 2 if it is even or 1 if it is odd.
#     """
#
#     if t == "e":
#         start = 2
#     elif t == "o":
#         start = 1
#     else:
#         return -1
#
#     return sum(range(start, n, 2))
#
#
# user_input = int(input("Enter to sum up in range: "))
# string_input = input("even or odd: ")
# print(sum_eo(user_input, string_input))
# # =======================================================
# # ----- AVERAGE MARKS USING DICTIONARIES AND LISTS -----
# if __name__ == '__main__':
#     n = int(input())
#     average1 = 0
#     average2 = 0
#     student_marks = {}
#     for i in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     student_name = input()
#     # print(student_marks)
#     # print(student_name)
#     if student_name in student_marks.keys():
#         for marks in student_marks[student_name]:
#             average1 += marks
#             average2 = average1/3
#
#     print("{:.2f}".format(average2))
# # =======================================================
# # ----- LIST FUNCTIONS -----
# empty_list = []
# n = int(input())
# for i in range(n):
#     splitting = input().split()
#     if splitting[0] == "insert":
#         empty_list.insert(int(splitting[1]), int(splitting[2]))
#     elif splitting[0] == "print":
#         print(empty_list)
#     elif splitting[0] == "remove":
#         empty_list.remove(int(splitting[1]))
#     elif splitting[0] == "append":
#         empty_list.append(int(splitting[1]))
#     elif splitting[0] == "sort":
#         empty_list.sort()
#     elif splitting[0] == "pop":
#         empty_list.pop()
#     elif splitting[0] == "reverse":
#         empty_list.reverse()
# # =======================================================

# Swap first and last digit of a number...

# num = input("Enter a number: ")
# # tmp = 0
# # swap the first and the last digits of the number
# arr = []
# for i in num:
#     arr.append(int(i))
#
# tmp = arr[0]
# arr[0] = arr[len(arr) - 1]
# arr[len(arr) - 1] = tmp
#
# for i in arr:
#     print(i, end="")

# # =======================================================

# Substring Problem

# Method 1:
# n1 = input()
# n2 = input()
# print(list(n1))
# print(list(n2))
# if n2 in n1:
#     print("its there")
# else:
#     print("not there")
#
# # Method 2:
# [n1, n2] = list(input().split())
# if n2 in n1:
#     print("its there")
# else:
#     print("not there")

# # =======================================================

# Trailing zeros of a factorial
# def fact(n: int) -> int:
#     if (n == 1) or (n == 0):
#         return 1
#     else:
#         return n * fact(n - 1)
# 
#
# def trailZero(n: int) -> int:
#     count = 0
#     while n > 0:
#         if n % 10 == 0:
#             count += 1
#             n /= 10
#         else:
#             break
#     return count
#
#
# num = int(input("enter a number: "))
# print(f"Number of trailing Zeros of {fact(num)} is {trailZero(fact(num))}")

# # ===========================================================
# Designer door mat
# M = int(input("Enter the one dimension: "))
# N = 3 * M
# half = int(M / 2)
#
# for i in range(half):
#     print((".|."*((2*i) + 1)).center(N, '-'))
#
# print("WELCOME".center(3 * M, '-'))
#
# for i in range(half, 0, -1):
#     print((".|."*((2*i) - 1)).center(N, '-'))
# # ===========================================================
# String formatting

# def print_formatted(n):
#     l = len(f"{n}")
#     for i in range(1, n+1):
#         print("{0:>{g}d} {0:>{g}o} {0:>{g}x} {0:>{g}b}".format(i, g=l))

# def print_formatted(n):
#     l = len(str(bin(n)))
#     for i in range(1, n+1):
#         print(str(i).rjust(l, ' '), oct(i)[2::].rjust(l, ' '), hex(i)[2::].rjust(l, ' ').upper(), bin(i)[2::].rjust(l, ' '))
#
#
# n = int(input())
# print_formatted(n)

# # ===========================================================

# arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
# 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# l = []
# n = int(input("enter size: "))
#
# for i in range(n):
#     l.append(arr[i])
#
# l.sort(reverse=True)
#
# m = l[::] + l[n - 2:: - 1]
# mid = '-'.join(m)
# length = len(mid)
# # print(mid)
# # print(length)
# # print(l[n - 5:: - 1])
# # print(l[:n - 3])
# if n == 1:
#     print(l[0])
# else:
#     for i in range(1, n):
#         print('-'.join(l[:n - (n - i + 1)] + l[n - (n - i + 1)::-1]).center(length, '-'))
#
#     for i in range(n, 0, -1):
#         print('-'.join(l[:n - (n - i + 1)] + l[n - (n - i + 1)::-1]).center(length, '-'))

# # ===========================================================
#  Word capitalize
# arr = []
# s = input("enter something: ")
# n = len(s.split(" "))
# for ele in s.split(" "):
#     a = ele.capitalize()
#     arr.append(a)
#
# print(" ".join(arr))


# t = [{
#     'name' : 'Rohith',
#     'post' : 'President',
#     'dept' : 'CSE',
#     'year' : 4,
#     'sec' : 'A',
# },
#     {
#         'name' : 'Jiva',
#         'post' : 'Vice president',
#         'dept' : 'cse',
#         'year' : 4,
#         'sec' : 'B',
#     },
#     {
#         'name' : 'Yuvanshankar',
#         'post' : 'Secretary',
#         'dept' : 'CSE',
#         'year' : 4,
#         'sec' : 'C',
#     },
#     {
#         'name' : 'Mohammed Irfan Khan',
#         'post' : 'President',
#         'dept' : 'CSE',
#         'year' : 4,
#         'sec' : 'C',
#     },]
#
# for i in range(len(t)):
#     if t[i]["dept"].islower():
#         b = t[i]["dept"].upper()
#     t[i].update()
# print(t)
# # ===========================================================
"""Question 2"""

# str_List = []
# int_List = []
# a = input("Enter the string with Alphanumeric characters: ").split()
# for i in range(len(a)):
#     if a[i].isnumeric():
#         int_List.append(a[i])
#     else:
#         str_List.append(a[i])
#
# print("Length of integers:", len(" ".join(int_List)))
# print("Lenght of alphabets:", len(" ".join(str_List)))


# # ===========================================================

"""Question 4"""

# str_tuple = []
# int_list = []
# int_set = []
#
# n = int(input("Enter the range: "))
#
# for i in range(n):
#     a = input("Enter string: ")
#     str_tuple.append(a)
#     b = int(input("Enter integer: "))
#     if b > 0:
#         int_list.append(b)
#     else:
#         int_set.append(b)
#
# print(tuple(str_tuple))
# print(int_list)
# print(set(int_set))
# # ===========================================================

# """Question 1"""
#
# # # Question 1
# d1 = {"name": "Krish",
#       "class": "CSE",
#       "section": "A",
#       "roll number": 23}
#
# d2 = {"name": "Rahul",
#       "class": "ECE",
#       "section": "B",
#       "roll number": 41}
#
# d3 = {"name": "Lilly put",
#       "class": "AI & DS",
#       "section": "A",
#       "roll number": 26}

# # Question 2
# print(d1.values())
# print()
# print(d2.values())
# print()
# print(d3.values())

# # Question 3
# d1["marks"] = 78
# d2["marks"] = 89
# d3["marks"] = 75

# print(d1)
# print(d2)
# print(d3)

# # Question 4
# l = []
# p = d1["marks"]
# q = d2["roll number"]
# r = d3["section"]
# l.append(p)
# l.append(q)
# l.append(r)
# del d1["marks"]
# del d2["roll number"]
# del d3["section"]
#
# print(l)

# # Question 5
# d4 = {"name" : {d1["name"], d2["name"], d3["name"]},
#       "class": {d1["class"], d2["class"], d3["class"]},
#       "section": {d1["section"], d2["section"], d3["section"]},
#       "roll no": {d1["roll number"], d2["roll number"], d3["roll number"]},
#       "marks": {d1["marks"], d2["marks"], d3["marks"]}}
#
# print(d4)
# # ===========================================================

"""Question 5"""
# # 3 X 3
# m1 = [[12, 7, 3],
#       [4, 5, 6],
#       [7, 8, 9]]
#
# # 3 x 4
# m2 = [[5, 8, 1],
#       [6, 7, 3],
#       [4, 5, 9]]
#
# res = [[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0]]
#
# for i in range(len(m1)):
#     for j in range(len(m2[0])):
#         for k in range(len(m2)):
#             res[i][j] += m1[i][k] * m2[k][j]
#
# for ele in res:
#     print(ele)

# # ===========================================================
# Frequency sort
# def recent(n: str):
#       a = {}
#       for ele in n:
#             a[ele] = 0
#       for ele in n:
#             if ele in n:
#                   a[ele] += 1
#             else:
#                   a[ele] = 1
#
#       b = sorted(a.items(), key=lambda item: item[1], reverse=True)
#       for i in b:
#             print(f"{i[0]} = 0{i[1]}")
#
#
# string = input("enter the string: ")
# recent(string)

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

