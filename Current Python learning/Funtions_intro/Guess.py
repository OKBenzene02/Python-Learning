import random

def get_integer(we_need):
    """
    we get an integer value which is an (stdin).

    this programme will continue looping the user
    provides an valid integer rather than the string.

    :param we_need:the string the user will see,
        when they are prompted.
    :return:the integer the user enters.

    """
    while True:
        ok = input(we_need)
        if ok.isnumeric():
            return int(ok)
        else:
            print("please enter a number")

print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)


highest = 10
answer = random.randint(1, highest)
print(answer)     # TODO:Remove after testing

print("please enter a number between 1 to {}:".format(highest))
guess = 0
while guess != answer:
    guess = get_integer("Please guess a number: ")

    if guess == answer:
        print("well done you got it correct.")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")


# import random
#
# highest = 21
# answer = random.randint(11, highest)
# print(answer)
# print("please enter a number between 11 to {}.".format(highest))
#
# guess = 0
#
# while guess != answer:
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it correctly")
#         break
#     else:
#         if guess > answer:
#             print("please guess lower")
#         else:
#             print("please guess higher")
























