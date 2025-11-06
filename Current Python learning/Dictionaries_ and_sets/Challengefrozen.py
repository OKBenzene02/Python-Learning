# user_input = input("please enter a text: ")
# vowels = frozenset("aeiou")
# remover = sorted(set(user_input).difference(vowels))
#
# print(remover)
# veg = {"cabbage": "healthy for all",
#        "sprouts": "very healthy seeds",
#        "spinach": 'helps you grow tall'}
# print(veg.keys())
# print(veg.values())
# for veggies in veg.keys():
#     print(veggies)
# for values in veg.values():
#     print(values)

# empty_dic = {}
# marks = []
# scores = 0
# n = int(input("enter the range: "))
# for i in range(n):
#     name = input("enter name: ")
#     scores = float(input("marks: "))
#     empty_dic[name] = scores
#
# print(empty_dic)

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
