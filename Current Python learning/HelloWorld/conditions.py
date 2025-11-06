# age = int(input("How old are you? "))
# # if age <= 65 and age >= 18:
# # if 16 <= age <= 65:
# if age in range(16, 66):
#     print("have a good day at work.")
# else:
#     print("sleep well.")
#
# if 16 < age < 66:
#     print("have a good day at work")
# else:
#     print("sleep well")

# =============================================
# # ----- GREATEST OF THREE NUMBERS ------
# a = int(input("Enter a number A: "))
# b = int(input("Enter a number B: "))
# c = int(input("Enter a number C: "))
#
# # if a > b and a > c:
# #     print("{} is greater.".format(a))
# # elif b > a and b > c:
# #     print("{} is greater.".format(b))
# # else:
# #     print("{} is greater.".format(c))
#
# if a > b and a > c:
#     if a > 0:
#         print("a is greater and positive.")
#     elif a < 0:
#         print("a is greater and negative.")
# if a < b and c < b:
#     if b > 0:
#         print("b is greater and positive.")
#     elif b < 0:
#         print("b is greater and negative.")
# elif c > a and c > b:
#     if c > 0:
#         print("c is greater and positive.")
#     elif c < 0:
#         print("c is greater and negative.")
# ===========================================


# n = int(input())
# count = 0
# empty_list = []
# happy_list = []
# for i in range(n):
#     string = input()
#     if string[0] == "!":
#         happy_list.append(string)
#     else:
#         empty_list.append(string)
#
# # print(happy_list)
# # print(empty_list)
# count = 0
# for i in empty_list:
#     for j in happy_list:
#         if j == "!" + i:
#             count += 1
#             continue
#
# if count != 0:
#     print("happy")
# else:
#     print("unhappy")

