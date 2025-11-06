# # -----LEAP YEAR-----
# print("----> LEAP YEAR <----")
# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("{} is a Leap year.".format(year))
#         else:
#             print("{} is not a leap year.".format(year))
#     else:
#         print("{} is a leap year.".format(year))
# else:
#     print("{} is not a leap year.".format(year))

# # ---- LEAP YEAR USING FUNCTIONS ----
# def is_leap(year):
#     leap = False
#
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
#
#     return leap
#
# year = int(input())
# print(is_leap(year))

# # =======================================================
# # ----- MULTIPLICATION TABLE ------
# print("="*40)
# for i in range(1, 3):
#     for j in range(1, 11):
#         print("\t{} x {} = {}\t".format(i, j, i * j))
#     print("=" * 40)
# # # =======================================================
# # ---- FIBONACCI SERIES USING RECURSION -----
# def fibbo(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibbo(n - 1) + fibbo(n - 2))
#
#
# terms = int(input("Enter the range: "))
# if terms < 0:
#     print("Enter positive range.")
# else:
#     print("Fibonacci series")
#     for i in range(terms + 1):
#         print(i, fibbo(i))
# # =======================================================
# # ---- SIMPLE CALCULATOR ----
# def add(a, b):
#     return a + b
# def minus(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a/b
#
# print(add(2, 3))
# print(multiply(2, 3))
# print(minus(2, 3))
# print(divide(2, 3))
# # =======================================================
# # ---- MAX AND MIN OF A LIST ----
# num = [1, 2, 3]
# some = ['this', 'ok', 'apple']
# print(max(num))
# print(min(num))
# print(min(some))
# print(max(some))
# # =======================================================
# # ---- SLICES ----
# string = "Crescent University"
# print(string[0])
# print(string[0:2])
# print(string[-1:0])
# print(string[:-4])
# print(string[:])
# # =======================================================
# # ---- OPERATORS ----
# print(2-3 ** 4/8+2 * 4 ** 5 * 1 ** 8)
# print(4 + 2 - 10 / 2 * 4 ** 2)
# # =======================================================
# # ---- RESULTS PRINT ----
# import random
# student_id = random.randint(1, 5)
# print("Student ID: {}".format(student_id))
#
# name = input("Enter your name: ")
# input_id = int(input("Enter student ID: "))
#
# if input_id == student_id:
#     print("-----> Authorised <----")
#     print("Enter your marks: ")
#     math = int(input("Maths: "))
#     phy = int(input("Physics: "))
#     chem = int(input("Chemistry: "))
#     computer = int(input("Computer science: "))
#     marks = int(math + phy + chem + computer)
#     percentage = (marks/400) * 100
#     cgpa = percentage/9.5
#     print("Name:", name)
#     print("Student ID:", input_id)
#     print("Marks: {}/400".format(marks))
#     print("Percentage:{:.2f}%".format(percentage))
#     print("CGPA: {:.1f}".format(cgpa))
#     if cgpa > 9:
#         print("S++ GRADE")
#     elif 7 < cgpa < 9:
#         print("S GRADE")
#     else:
#         print("I GRADE")
#
# else:
#     print("\tEnter valid Student ID\t")

# # ----- RESULTS USING LISTS -----

# subject_list = ["Maths", "Physics", "Chemistry", "Computer"]
# marks_list = []
# average1 = 0
# average = 0
# percentage = 0
# name = input("Enter your name: ")
# RRN = int(input("RRN: "))
# for i in subject_list:
#     marks = input()
#     marks_list.append([i, marks])
#
# for i in marks_list:
#     average += int(i[1])
#
# percentage = (average/200) * 100
#
# print("Name:", name)
# print("RRN:", RRN)
# for i in marks_list:
#     print("{} = {}".format(i[0], i[1]))
# print("Marks:", average)
# print("Percentage:", percentage)
# if 90 <= percentage <= 100:
#     print("GRADE S+")
# elif 80 <= percentage < 90:
#     print("GRADE S")
# elif 70 <= percentage < 80:
#     print("GRADE E")
# elif percentage < 70:
#     print("GRADE I")

# # ---- CONCEPT FOR MARKS AND AVERAGE ----
# subject_list = ["Maths", "Physics", "Chemistry", "Computer"]
# marks_list = []
# for i in subject_list:
#     marks = input()
#     marks_list.append([i, marks])
#
# for i in marks_list:
#     print("{} = {}".format(i[0], i[1]))

# # =======================================================
""""
CONVERTING:
MONTHS TO MILLISECONDS
HOUR TO MILLISECONDS
DAY TO MILLISECONDS
A WEEK TO MILLISECONDS
MONTH TO MILLISECONDS
YEAR TO MILLISECONDS
"""
# print("""
# CONVERSIONS IN MILLISECONDS:
# one min = 60000
# one hour = 3600000
# one day = 86400000
# one week = 604800000
# one month = 2592000000
# one year = 31536000000
# """)
# print("""
# Available units:
# \tM: Minutes
# \tH: Hour
# \tD: Days
# \tW: Weeks
# \tN: Months
# \tY: Year
# """)
# conversion = input("Enter a time to convert: ")
# units = conversion[-1]
# number = float(conversion[:-1])
#
# onemin = 60000
# onehour = 3600000
# oneday = 86400000
# oneweek = 604800000
# onemonth = 2592000000
# oneyear = 31536000000
# if units.upper() == "M":
#     minu_to_milli = number * 60000
#     print("{}Minute = {:.3f}mS".format(number, minu_to_milli))
#     if onemin > minu_to_milli:
#         print("{} is greater than {}.".format(onemin, minu_to_milli))
#     else:
#         print("{} is lesser than {}.".format(onemin, minu_to_milli))
# elif units.upper() == "H":
#     hour_to_milli = float(number * 3600000)
#     print("{}Hour = {:.3f}mS".format(number, hour_to_milli))
#     if onehour > hour_to_milli:
#         print("{} is greater than {}.".format(onehour, hour_to_milli))
#     else:
#         print("{} is lesser than {}.".format(onehour, hour_to_milli))
# elif units.upper() == "D":
#     day_to_milli = float(number * 86400000)
#     print("{}Day = {:.3f}mS".format(number, day_to_milli))
#     if oneday > day_to_milli:
#         print("{} is greater than {}.".format(oneday, day_to_milli))
#     else:
#         print("{} is lesser than {}.".format(oneday, day_to_milli))
# elif units.upper() == "W":
#     week_to_milli = float(number * 86400000 * 7)
#     print("{}Week = {:.3f}mS".format(number, week_to_milli))
#     if oneweek > week_to_milli:
#         print("{} is greater than {}.".format(oneweek, week_to_milli))
#     else:
#         print("{} is lesser than {}.".format(oneweek, week_to_milli))
# elif units.upper() == "N":
#     month_to_milli = float(number * 86400000 * 30)
#     print("{}Month = {:.3f}mS".format(number, month_to_milli))
#     if onemonth > month_to_milli:
#         print("{} is greater than {}.".format(onemonth, month_to_milli))
#     else:
#         print("{} is lesser than {}.".format(onemonth, month_to_milli))
# elif units.upper() == "Y":
#     year_to_milli = float(number * 86400000 * 365)
#     print("{}Year = {:.3f}mS".format(number, year_to_milli))
#     if oneyear > year_to_milli:
#         print("{} is greater than {}.".format(oneyear, year_to_milli))
#     else:
#         print("{} is lesser than {}.".format(oneyear, year_to_milli))

# # =======================================================
# # ------ CURRENT BILL (TAMIL NADU) -------
# serno = int(input("Enter service Number : "))
# cname = input("Enter User Name : ")
# old = int(input("Enter your old reading : "))
# new = int(input("Enter your new reading : "))
#
# units = new-old
#
# if units <= 100:
#     amount = units*0.90
#     serchg = 25
# elif units >= 100 and units < 300:
#     amount = units*1.50
#     serchg = 35
# elif units >= 300 and units <= 500:
#     amount = units*2.75
#     serchg = 45
# elif units > 500:
#     amount = units*4.50
#     serchg = 100
#
# netamount = amount + serchg
#
# print("Electrical information : ")
#
# print("\tMeter Number : ", serno)
# print("\tUser Name : " + cname)
# print("\tOld reading : ", old)
# print("\tNew reading : ", new)
# print("\tTotal units : ", units)
#
# print("\n\tTotal payable amount : Rs.", netamount)
# # =======================================================

